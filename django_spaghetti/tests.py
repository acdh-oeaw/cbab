from django.contrib.auth.models import User
from django.test import Client, TestCase


class WebpageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_webpage(self):
        response = self.client.get('/datamodel/')
