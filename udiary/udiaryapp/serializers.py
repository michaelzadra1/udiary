from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from udiaryapp.models import Account
from entries.models import Entry, Analysis

class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)
	
	class Meta:
		model = Account
		fields = ['id', 'Email', 'created_at', 'updated_at', 'FName', 'LName', 'Gender', 'password', 'confirm_password']
		
		read_only_fields = ['id', 'created_at', 'updated_at']

		
		def create(self, validated_data):
			return Account.objects.create(**validated_data)
			
		def update(self, instance, validated_data):
			password = validated_data.get('password', None)
			confirm_password = validated_data.get('confirm_password', None)

			if password and confirm_password and password == confirm_password:
				instance.set_password(password)
				instance.save()

				update_session_auth_hash(self.context.get('request'), instance)

			return instance	
			
