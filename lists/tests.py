from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest (TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		print ("\n\n\n123: " + str(found.func))
		self.assertEquals(found.func, home_page)