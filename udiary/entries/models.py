from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from udiaryapp.models import Account


class Entry(models.Model):
	Account = models.ForeignKey(Account, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	Text = models.TextField()
	Complete = models.BooleanField(default=False)
	
	def __unicode__(self):
		return '{0}'.format(self.Text)
		
	def __str__(self):
		return self.Account + " " + self.Text[:50] + '...'

	def setComplete(self):
		self.Complete = True
		self.save()
		self.analyze()
		
	def analyze(self):
		#this will contain the code to run the api call(s) and save the results as an Analysis record
		pass
		
	def edit(self, text):
		self.Text = text
		self.Complete = False
		self.save()
		
class Analysis(models.Model):
	entry = models.ForeignKey(Entry, on_delete = models.CASCADE)
	updated_at = models.DateTimeField(auto_now=True)
	sentiment = models.TextField(default='');
	texttags = models.TextField(default='');
	keywords = models.TextField(default='');
	people = models.TextField(default='');
	places = models.TextField(default='');
	personality = models.TextField(default='');
	emotion = models.TextField(default='');
	personas = models.TextField(default='');
	
	sentiment_tags = models.TextField(default='');
	sentiment_keywords = models.TextField(default='');
	sentiment_people = models.TextField(default='');
	sentiment_places = models.TextField(default='');
	emotion_tags = models.TextField(default='');
	emotion_keywords = models.TextField(default='');
	emotion_people = models.TextField(default='');
	emotion_places = models.TextField(default='');
	
	def __str__(self):
		return self.id + " " + self.entry;
