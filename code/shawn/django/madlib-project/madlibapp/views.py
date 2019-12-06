from django.shortcuts import render, get_object_or_404
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
        context = { 'this_madlib': get_object_or_404(MadLib, pk=madlib_id), 
                    'this_madlib_id': madlib_id}

    # empty context if starting new
    else: 
        context = { 'this_madlib_id': 0}

    # render edit.html template
    return render(request, 'madlibapp/edit.html', context)

# intermediate/hidden view for applying changes to madlib
def hidden_edit(request, madlib_id):

    # get the input title
    input_title = request.POST['madlibtitle']

    # get input text
    input_string = request.POST['madlibtextarea']

    # if madlib_id is zero, create new madlib
    if madlib_id == 0:
        # create new MadLib
        m = MadLib.objects.create(title=input_title, text=input_string)
        # parse the input text to populate with MadLibWords
        m.parse_text()

    # else, edit existing MadLib in the db
    else:
        # get madlib, update title/text, then save
        this_madlib = get_object_or_404(MadLib, pk=madlib_id)
        this_madlib.text = input_string
        this_madlib.title = input_title
        this_madlib.save()

        # parse the input text to populate with MadLibWords
        this_madlib.parse_text()

    return HttpResponseRedirect(reverse('madlibapp:index'))

# a function for deleting MadLibs
def hidden_delete(request, madlib_id):

    # get the madlib
    delete_me = get_object_or_404(MadLib, pk=madlib_id)
    # delete the madlib from db
    delete_me.delete()

    # redirect to index
    return HttpResponseRedirect(reverse('madlibapp:index'))

# playing a madlib
def play(request, madlib_id):

    # get this MadLib. store as variable so that it's MadLibWords can also be retrieved
    this_madlib = MadLib.objects.get(pk=madlib_id)

    # get input MadLib and all it's MadLibWords from db, load into context
    context = { 'this_madlib': this_madlib } 
                # 'this_madlib_words': MadLibWord.objects.filter(madlib=this_madlib)}

    # render edit.html template
    return render(request, 'madlibapp/play.html', context)

# viewing a madlib 
def view(request, madlib_id):

    # get input MadLib from db, load into context
    context = { 'this_madlib': MadLib.objects.get(pk=madlib_id) }
    # render view.html template
    return render(request, 'madlibapp/view.html', context)
