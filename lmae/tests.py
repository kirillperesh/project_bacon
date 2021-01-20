from django.test import TestCase, SimpleTestCase, Client
# from .views import *

class BasicTest(SimpleTestCase):
    def setUp(self):
        # Every test needs a client
        self.client = Client()
        self.var = 5

    def test_self(self):
        self.assertEqual(self.var, 5)
    
    def test_home(self):        
        response = self.client.get('/')
        self.assertContains(response, "Hello, Django!")
