# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render,redirect
from .models import Question
from .forms import QuestionForm

# Create your views here.

def question_list(request):
	questions=Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'question/question_list.html',{'questions':questions})

def question_new(request):
	if request.method=="POST":
		form=QuestionForm(request.POST)
		if form.is_valid():
			question=form.save(commit=False)
			question.author=request.user
			question.published_date=timezone.now()
			question.save()
			# return redirect('question_detail', pk=question.pk)
	else:	
		form=QuestionForm()
	return render(request,'question/question_edit.html',{'form':form})

