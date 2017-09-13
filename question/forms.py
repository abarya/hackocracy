from django import forms
from django.contrib.auth.models import User
from .models import Question

class QuestionForm(forms.ModelForm):

	class Meta:
		model=Question
		fields=('title','description',)

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','password']	
