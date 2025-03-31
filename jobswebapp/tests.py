from django.test import TestCase
from unittest.mock import MagicMock
import sys
#from jobswebapp.models import Job

sys.modules['whitenoise'] = MagicMock()

class MyJobBoardTests(TestCase):
    def setUp(self):
        #job = Job()
        pass

    def test_main_list_url_returns_success(self):
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code,200)
        
