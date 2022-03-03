from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response,Http404,HttpResponseRedirect

from .models import Question
from django.utils import timezone
from django.template import loader
from .forms import questionForm

def index(request):
    listQ = Question.objects.all()
    template = loader.get_template('caprisun/index.html')
    form = questionForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/caprisun')
    context = {
        'listQ': listQ,
        'form': form,
    }
    
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'caprisun/detail.html', {'question': question})

def update(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    form = questionForm(request.POST, instance=question)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/caprisun')
    template = loader.get_template('caprisun/update.html')
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))

def delete(request, question_id):
    trash = get_object_or_404(Question, pk=question_id)
    trash.delete()
    return HttpResponseRedirect('/caprisun')

"""def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'index.html', {'form': form})"""

