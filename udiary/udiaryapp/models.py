from django.db import models

# Create your models here.
class User(models.Model): 
	FName = models.CharField(max_length=20)
	LName = models.CharField(max_length=30)
	DOB = models.DateTimeField('date of birth')
	Gender = models.CharField(max_length = 1)
	
	def __str__(self):
		return self.FName +self.LName

class Entry(models.Model):
	User = models.ForeignKey(User, on_delete = models.CASCADE)
	Date = models.DateTimeField('date added')
	Text = models.TextField()
	
	def __str__(self):
		return self.User + " " + self.Text[:50] + '...'
	
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
		