from django.test import Client, TestCase

# to run tests use command below, a html cover report will be available at: cover/index.html
# python manage.py test --settings=cbab.settings.test


class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search CBAB Database for")
