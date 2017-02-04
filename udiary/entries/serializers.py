from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from entries.models import Entry, Analysis

class EntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entry
		fields = ('id', 'Account', 'created_at', 'Text', 'Complete') 
		
		read_only_fields = ('id', 'created_at', 'updated_at')
		
		def create(self, validated_data):
			return Entry.objects.create(**validated_data)	

class AnalysisSerializer(serializers.ModelSerializer):
	class Meta:
		model = Analysis
		fields = ('entry', 'sentiment', 'texttags', 'keywords', 'people', 'places', 'personality', 'emotion', 'personas',)

		