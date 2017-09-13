    # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
# Create your views here.

def question_list(request):
        questions=Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'question/question_list.html',{'questions':questions})

def question_new(request):
        return render(request,'question/question_edit.html',{})

def add_ques(request):
    question = Question()
    question.title = request.POST.get("title1","null")
    question.description = request.POST.get("desc","null")
    question.author = request.user
    question.num_ans = 0
    question.published_date = timezone.now()
    question.save()
    url = "/"
    return HttpResponseRedirect(url)


def details(request,ques_id):
    question = get_object_or_404(Question, id=ques_id)
    return render(request,'question/details.html', {'question':question})

def add_ans(request):
    ques_id = request.POST["_ques"]
    ans = request.POST["ans"]

    question = Question.objects.filter(id=ques_id)[0]
    answer = Answer()
    answer.ans_desc=ans
    answer.ques = question
    answer.save()

    url = "/" + str(ques_id) +"/"
    return HttpResponseRedirect(url)
    #context = {'question:question'}
    #template = loader.get_template("question/details.html")
    #return HttpResponse(template.render(context, request))