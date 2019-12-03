import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for question for whose pub_date is in the future.
        """
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_a_recent_question(self):
        """
        was_published_recently() returns False for question for whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=58)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_a_past_question(self):
        """
        was_published_recently() returns False for question for whose pub_date is older than one day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Polls Are Available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past Question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Past Question.")
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])

    def test_future_question(self):
        create_question(question_text="Future Question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No Polls Are Available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        create_question(question_text="Past Question.", days=-30)
        create_question(question_text="Future Question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Past Question.")
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])

    def test_two_past_questions(self):
        create_question(question_text="Past Question. 1", days=-30)
        create_question(question_text="Past Question. 2", days=-7)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Past Question. 1")
        self.assertContains(response, "Past Question. 2")
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question. 2>', '<Question: Past Question. 1>'])
        