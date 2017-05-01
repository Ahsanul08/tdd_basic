from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from lists.views import home_page


class MVCTest(TestCase):

    def test_proper_view_function_resolved_by_url(self):
        found = resolve('/')
        print(found, type(found))
        self.assertEqual(found.func, home_page)