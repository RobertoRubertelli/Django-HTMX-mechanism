from django.test import TestCase , SimpleTestCase

from django.urls import reverse

# Create your tests here.

class HomeTests(SimpleTestCase):

    def test_home_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
