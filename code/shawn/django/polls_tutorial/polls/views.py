from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect       # for functional views
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic                                            # for class-based views
from .models import Question, Choice                                        # import our models
# from django.template import loader                                        # for the non-shortcut method
from django.shortcuts import render


# CLASS BASED VIEWS
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]  # the list of data to send to HMTL template
        
class DetailView(generic.DetailView):
    template_name = 'polls/details.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())            # the list of data that will be used to search detail view

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# actual voting request/response.  
def vote(request, question_id):

    # get question from db, with error handling
    question = get_object_or_404(Question, pk=question_id)

    #try/except to make sure we get valid input from the form
    try:         
        # get choice from body of the request (which was the form input)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 
                    'polls/details.html', 
                    {'question':question, 'error_message': "Please make a selection...."})

    # increment number of votes in database
    selected_choice.votes += 1 

    # save change to db
    selected_choice.save()

    # redirect to results page (so that there's no risk of reload/resubmitting the form)
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))






# REPLACING ALL OF THIS CODE BELOW USING GENERIC CLASS TEMPLATES
# BELOW ARE "FUNCTION BASED" VIEWS
# home page: displays the last few questions posted
# def index(request):

#     # get data from model/do calculations
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     # get html template
#     # template = loader.get_template('polls/index.html')         # for the non-shortcut method

#     # set context
#     context = {
#         'latest_question_list': latest_question_list,
#     }

#     # return html template response with context
#     # return HttpResponse(template.render(context,request))         # this is the non-shortcut method
#     return render(request,'polls/index.html', context)

# # detail page: looks at given question and it's answers 
# def detail(request, question_id):
    
#     # try to find question from database
#     #                   shortcut method
#     question = get_object_or_404(Question, pk=question_id)         
#     #                   non-shortcut method 
#     # try: 
#     #     question = Question.objects.get(pk=question_id)
#     # # if the question can't be found in database, raise 404 error
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist.")

#     # get choices that match with the question 
#     # don't need to do it this way, instead can do reverse lookup through Django....question.choices_set.all()
#     # choices = Choice.objects.filter(question_id=question_id)        

#     context = { 'question': question,
#                 # 'choice_list': choices
#               }
#     return render(request, 'polls/details.html', context)

# # results page: where you go after you cast a vote
# # this has all the shortcut versions
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


