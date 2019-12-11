import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Choice, Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future
    
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is within the last day.

        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    def test_was_published_recently_with_past_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than one day.
    
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)
    
class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_question_and_past_question(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Past question.")
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-7)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Past question 1.")
        self.assertContains(response, "Past question 2.")
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>'])

class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:detail', args=(future_question.pk,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:detail', args=(past_question.pk,)))
        self.assertContains(response, past_question.question_text)
