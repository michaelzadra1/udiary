from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	def create_account(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('User must have a valid email address')
		
		if not kwargs.get('dob'):
			raise ValueError("User must provide a date of birth")
		
		account = self.model(
			email = self.normalize_email(email), dob = kwargs.get('dob')
			)
		account.set_password(password)
		account.save()
		
		return account
		
# Create your models here.
class Account(AbstractBaseUser): 
	FName = models.CharField(max_length=20)
	LName = models.CharField(max_length=30)
	Email = models.EmailField(unique=True)

	DOB = models.DateTimeField('date of birth')
	Gender = models.CharField(max_length = 1)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()
	
	USERNAME_FIELD = 'Email'
	REQUIRED_FIELDS= ['email', 'DOB']
	
	def __str__(self):
		return self.FName +self.LName

	def __unicode__(self):
		return self.email
		
	def get_full_name(self):
		return self.FName + " " + self.LName
		
	def get_short_name(self):
		return self.FName

		

	