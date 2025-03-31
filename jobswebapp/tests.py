from django.test import TestCase
#from jobswebapp.models import Job

class MyJobBoardTests(TestCase):
    def setUp(self):
        #job = Job()
        pass

    def test_main_list_url_returns_success(self):
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code,200)
        
