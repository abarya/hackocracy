from django.db import models
from django.utils import timezone

class Question(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=200)
	description=models.TextField()
	published_date=models.DateTimeField(blank=True,null=True)
	num_ans = models.IntegerField()
	#TODO
	#tags
	#answers

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Answer(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_desc = models.TextField(max_length=1000)
    #ans_date = models.DateTimeField(blank=True,null=True)