from django.test import Client, TestCase


class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search CBAB Database for")
