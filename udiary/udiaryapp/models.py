from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	def create_user(self, **kwargs):
		#if not email:
		#	raise ValueError('User must have a valid email address')
		
		account = self.model(
			Email = self.normalize_email(kwargs.get('Email'))
			)
		account.set_name_gender(kwargs.get('FName'), kwargs.get("LName"), kwargs.get('Gender'))
		account.set_password(kwargs.get('password'))
		account.save()
		
		return account
		
# Create your models here.
class Account(AbstractBaseUser): 
	FName = models.CharField(max_length=20)
	LName = models.CharField(max_length=30)
	Email = models.EmailField(unique=True)

	Gender = models.CharField(max_length = 1)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()
	
	USERNAME_FIELD = 'Email'
#	REQUIRED_FIELDS= ['Email']
	
	def __str__(self):
		return self.FName +self.LName

	def __unicode__(self):
		return self.email
		
	def get_full_name(self):
		return(self.FName + " " + self.LName)
		
	def get_short_name(self):
		return self.FName
		
	def set_name_gender(self, f, l, g):
		self.FName = f
		self.LName = l
		self.Gender = g

	