from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from analysis.models import Analysis


class AnalysisSerializer(serializers.ModelSerializer):
	class Meta:
		model = Analysis
		fields = ('entry', 'sentiment', 'texttags', 'keywords', 'people', 'places', 'personality', 'emotion', 'personas', 'sentiment_tags', 'sentiment_keywords', 'sentiment_people', 'sentiment_places',)
		read_only_fields = ('id', 'updated_at')
		
		def create(self, validated_data):
			return Analysis.objects.create(**validated_data)