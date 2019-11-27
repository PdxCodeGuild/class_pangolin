from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# from django.template import loader                            # for the non-shortcut method
from django.shortcuts import render

# home page: displays the last few questions posted
def index(request):

    # get data from model/do calculations
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # get html template
    # template = loader.get_template('polls/index.html')         # for the non-shortcut method

    # set context
    context = {
        'latest_question_list': latest_question_list,
    }

    # return html template response with context
    # return HttpResponse(template.render(context,request))         # this is the non-shortcut method
    return render(request,'polls/index.html', context)

# detail page: looks at given question and it's answers 
def detail(request, question_id):
    return HttpResponse(f"You're looking at the details of question {question_id}.")

# results page: where you go after you cast a vote
def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

# actual voting request/response.  
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
