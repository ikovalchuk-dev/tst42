from django.test import TestCase
from django.test.client import Client


class IndexViewTest(TestCase):
    def test_index(self):
        cli = Client()
        response = cli.get('/')
        self.assertEqual(response.status_code, 200)
