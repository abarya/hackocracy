from django import forms
from django.contrib.auth.models import User

class UserFormSignUp(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','password']	

class UserFormSignIn(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','password']	
