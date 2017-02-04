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
	sentiment = models.TextField();
	texttags = models.TextField();
	keywords = models.TextField();
	people = models.TextField();
	places = models.TextField();
	personality = models.TextField();
	emotion = models.TextField();
	personas = models.TextField();

	def __str__(self):
		return self.id + " " + self.entry;
