import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() returns False for questions whose pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''
        was_published_recently() returns True for questions whose pub_date is recent...one second less than a day
        '''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_past_question(self):
        '''
        was_published_recently() returns True for questions whose pub_date is not so recent (one second over one day)
        '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):

    # no questions
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))                      # get the polls index route from client
        self.assertEqual(response.status_code, 200)                             # check for good response code
        self.assertContains(response, "No polls are available")                # look to see if the html rendered contains "no polls" string
        self.assertQuerysetEqual(response.context['latest_question_list'],[])   # check to see that no questions case returns empty query set

    # multiple past questions
    def test_past_question(self):
        create_question(question_text="Past Question.", days=-30)               # create dummy past question
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question.>'])

    # past and future questions
    def test_future_question(self):
        create_question(question_text="Future Question.", days=30)               # create dummy past question
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")                # look to see if the html rendered contains "no polls" string
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # past questions
    def test_future_question_and_past_question(self):
        create_question(question_text="Past Question", days=-30)
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'Past Question')
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

    # future question
    def test_two_past_questions(self):
        # setup
        create_question(question_text="Past Question 1", days=-30)
        create_question(question_text="Past Question 2", days=-15)
        response = self.client.get(reverse('polls:index'))

        # assertions
        self.assertContains(response, 'Past Question 1')
        self.assertContains(response, 'Past Question 2')       
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question 2>', '<Question: Past Question 1>'])

class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        #setup
        future_question = create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))

        #test/assertion
        self.assertEqual(response.status_code, 404)

    def test_pass_question(self):
        # setup
        past_question = create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        
        #test/assertion
        self.assertContains(response, past_question.question_text)

