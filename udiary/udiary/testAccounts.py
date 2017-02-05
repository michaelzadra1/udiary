from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from udiaryapp.models import Account

class AccountTests(APITestCase):
	def test_create_account(self):
		"""
		Ensure we can create a new account object.
		"""
		url = '/api/v1/accounts/'
		data = {
			'Email': 'a@abc.com',
			'FName': 'John',
			'LName' : 'Doe',
			'Gender' :'M',
			'password':'pass',
			'confirm_password':'pass'
		}
		
		response = self.client.post(url, data, format='json')
		data2 = {
			'Email': 'b@abc.com',
			'FName': 'Jane',
			'LName' : 'Doe',
			'Gender' :'M',
			'password':'pass',
			'confirm_password':'pass'
		}
		
		response = self.client.post(url, data2, format='json')
		data3 = {
			'Email': 'c@abc.com',
			'FName': 'John',
			'LName' : 'Doe',
			'Gender' :'M',
			'password':'pass',
			'confirm_password':'pass'
		}
		
		response = self.client.post(url, data3, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Account.objects.count(), 3)

		objs = Account.objects.all()
		print(len(objs))
		for obj in objs:
			print("obj:" + obj.get_full_name())