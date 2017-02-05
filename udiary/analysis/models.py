from django.db import models
from entries.models import Entry
from django.contrib.postgres.operations import HStoreExtension

# Create your models here.
class Analysis(models.Model):
	entry = models.ForeignKey(Entry, on_delete = models.CASCADE, related_name='parent_entry') #can stay
	updated_at = models.DateTimeField(auto_now=True) #can stay
	sentiment = models.FloatField(default='');
	texttags = models.HStoreField(default='');
	keywords = models.HStoreField(default='');
	people = models.ArrayField(models.CharField());
	places = models.ArrayField(models.CharField());
	personality = models.HStoreField(default='');
	emotion = models.HStoreField(default='');
	personas = models.HStoreField(default='');
	
'''	
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
		'''
		
	def __str__(self):
		return self.id + " " + self.entry;

	def analyze(self, text):
		pass
