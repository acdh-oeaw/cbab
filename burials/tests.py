from django.test import TestCase

from django.contrib.auth.models import User
from django.test import Client, TestCase


class BurialsTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_superuser('temporary', 'temp@gmail.com', 'temporary')
        form_data = {'username': 'temporary', 'password': 'temporary'}
        self.client.post('/accounts/login/', form_data)

    def test_burrials(self):
        response = self.client.get('/burials/burialsite/create/')
        self.assertContains(response, 'Alternative name')
