from django.db import models
from entries.models import Entry
# Create your models here.
class Analysis(models.Model):
	entry = models.ForeignKey(Entry, on_delete = models.CASCADE, related_name='parent_entry')
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
	def __init__(self, text):
		self.analyze()
		
	def __str__(self):
		return self.id + " " + self.entry;

	def analyze(self, text):
		pass