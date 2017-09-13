    # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.shortcuts import render,redirect, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import QuestionForm,UserForm

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
                question.num_ans=0
                question.published_date=timezone.now()
                question.save()
                url = "/"
                return HttpResponseRedirect(url)
                # return redirect('question_detail', pk=question.pk)
        else:
            form=QuestionForm()
        return render(request,'question/question_edit.html',{'form':form})

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

class UserFormView(View):
	form_class=UserForm
	template_name='question/registration_form.html'

	#displays blank form
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process from data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned or normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:
					login(request,user)
					return redirect(question_list)
					
		return render(request,self.template_name,{'form':form})			

