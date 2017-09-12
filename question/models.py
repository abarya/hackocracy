from django.db import models
from django.utils import timezone

class Question(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=200)
	description=models.TextField()
	published_date=models.DateTimeField(blank=True,null=True)
	#TODO
	#tags
	#answers

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title	