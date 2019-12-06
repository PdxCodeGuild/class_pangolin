from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MadLib, MadLibWord

# index page will list all of the completed MadLibs
def index(request):

    # get all MadLibs in db, load into context
    context = { 'madlibs_list': MadLib.objects.all() }
    # render index.html template
    return render(request, 'madlibapp/index.html', context)

# creating/editing a template
def edit(request, madlib_id):

    # check to see if creating new madlib, in which case madlab_id would be 0
    if madlib_id != 0:
        # get input MadLib from db, load into context
        context = { 'this_madlib': MadLib.objects.get(pk=madlib_id)}

    # empty context if starting new
    else: 
        context = { 'this_madlib': 'new'}

    # render edit.html template
    return render(request, 'madlibapp/edit.html', context)

# intermediate/hidden view for applying changes to madlib
def hidden_edit(request, madlib_id):

    ###############
    # insert code here to create/edit a madlib
    ###############

    return HttpResponseRedirect(reverse('madlibapp:index'))

# playing a madlib
def play(request, madlib_id):

    # get this MadLib. store as variable so that it's MadLibWords can also be retrieved
    this_madlib = MadLib.objects.get(pk=madlib_id)

    # get input MadLib and all it's MadLibWords from db, load into context
    context = { 'this_madlib': this_madlib, 
                'this_madlib_words': MadLibWord.objects.filter(madlib=this_madlib)}

    # render edit.html template
    return render(request, 'madlibapp/edit.html', context)

# viewing a madlib 
def view(request, madlib_id):

    # get input MadLib from db, load into context
    context = { 'this_madlib': MadLib.objects.get(pk=madlib_id) }
    # render view.html template
    return render(request, 'madlibapp/edit.html', context)
