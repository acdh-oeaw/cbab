from django.contrib.auth.models import User
from django.test import Client, TestCase


class VocabsTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')
        form_data = {'username': 'temporary', 'password': 'temporary'}
        self.client.post('/accounts/login/', form_data)

    def test_vocabs(self):
        rv = self.client.get('/vocabs/scheme/')
        self.assertContains(rv, 'Concept Schemes')
        rv = self.client.get('/vocabs/scheme/create/', follow=True)
        self.assertContains(rv, 'Namespace')
