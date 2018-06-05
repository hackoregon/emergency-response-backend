from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient

class RootTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class RootEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/emergency/')
        assert response.status_code == 200
