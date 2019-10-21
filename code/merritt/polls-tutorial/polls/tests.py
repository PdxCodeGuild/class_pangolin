import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
    """Tests for Question model"""
    def test_was_published_recently_with_future_question(self):
        """if date is in future, was_published_recently() should return False"""
        time = timezone.now() + datetime.timedelta(weeks=1664)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """if date is older than one day, was_published_recently() should return False"""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """if date is within the past day, was_published_recently() should return True"""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59, milliseconds=999)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """create a question with text of 'question_text' and published 'days' number of days in past/future"""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    """
    no questions > display error message
    past question > display on page
    future question > display error message (no questions to show)
    one of each > display only past question
    two past > display both
    """
    def test_no_questions(self):
        """
        if no questions, display message
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        if past question, display on index page
        """
        create_question(question_text="Past question?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question?>'])

    def test_future_question(self):
        """
        if future question, display no questions found
        """
        create_question(question_text="Future question?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        if a future and a past question, only display past question
        """
        create_question(question_text="Past question?", days=-30)
        create_question(question_text="Future question?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question?>'])

    def test_two_past_questions(self):
        """
        index page will display multiple questions
        """
        create_question(question_text="Past question?", days=-30)
        create_question(question_text="Another past question?", days=-60)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question?>', '<Question: Another past question?>']
        )

class QuestionDetailViewTests(TestCase):
    """
    future question
    past question
    """
    
    def test_future_question(self):
        future_question = create_question(question_text="Future question?", days=61)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question?", days=-61)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultsViewTests(TestCase):
    """
    future question
    past question
    """
    
    def test_future_question(self):
        future_question = create_question(question_text="Future question?", days=61)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question?", days=-61)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)