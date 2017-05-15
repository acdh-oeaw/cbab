from django.contrib.auth.models import User
from django.test import Client, TestCase


class WebpageTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')

    def test_webpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search CBAB Database for')
        response = self.client.get('/accounts/login/')
        self.assertContains(response, 'Username')
        form_data = {'username': 'temporary', 'password': 'temporary'}
        response = self.client.post('/accounts/login/', form_data, follow=True)
        self.assertContains(response, 'temporary')
        response = self.client.get('/logout', follow=True)
        self.assertContains(response, 'signed out')
        form_data = {'username': 'non_exist', 'password': 'temporary'}
        response = self.client.post('/accounts/login/', form_data, follow=True)
        self.assertContains(response, 'user does not exist')
