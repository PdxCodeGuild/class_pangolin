from django.db import models
import datetime
from django.utils import timezone

# Create your models here. This will turn into SQLLite databses.  

class Question(models.Model):
    #Question class for poll
    question_text = models.CharField(max_length=200)
    #keeps track of when a poll is proposed, for database
    pub_date = models.DateTimeField('date published')

    #produce a string representation of the question object
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #Choice class for poll.  

    #Max characters for answer choices
    choice_text = models.CharField(max_length=200)

    

    #keeps track of number of votes
    votes = models.IntegerField(default=0)
    #If a question is deleted, all answer choices get deleted as well.  
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    
    #produce a string representation of the choice objects
    def __str__(self):
        return self.choice_text