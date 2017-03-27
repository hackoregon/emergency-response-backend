from django.test import TestCase
from data.models import Agency
from rest_framework.test import APIClient, RequestsClient

#Create your tests here.
class AgencyTestCase(TestCase):
    def test_agency_returns_attributes(self):
        agency = Agency.objects.get(agency_id=1)
        self.assertEqual(agency.agency_id, 1)
        self.assertEqual(agency.description, 'PORT OF PORTLAND')
        self.assertEqual(agency.statecode, '0291')

class AgencyEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/emergency/agencies/')
        assert response.status_code == 200
    def test_list_description__icontains_query_works(self):
        response = self.client.get('/emergency/agencies/?description__icontains=portland')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/emergency/agencies/1/')
        assert response.status_code == 200

class AlarmLevelsEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/emergency/alarmlevels/')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/emergency/alarmlevels/1/')
        assert response.status_code == 200

class FireBlocksEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/emergency/fireblocks/')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/emergency/fireblocks/471/')
        assert response.status_code == 200
    def geofilter_query_200_response(self):
        response = self.client.get('/emergency/fireblock/?lat=45.520697&lon=-122.677345')
        assert response.status_code == 200
    def test_geofilter_400_response(self):
        response = self.client.get('/emergency/fireblock/')
        assert response.status_code == 400
    def test_geofilter_404_response(self):
        response = self.client.get('/emergency/fireblock/?lat=-80.6875419&lon=40.032249')
        assert response.status_code == 404
    def fireblockincidents_query_200_response(self):
        response = self.client.get('/emergency/fireblock/incidents/?lat=45.520697&lon=-122.677345')
        assert response.status_code == 200
    def test_fireblockincidents_400_response(self):
        response = self.client.get('/emergency/fireblock/incidents/')
        assert response.status_code == 400
    def test_fireblockincidents_badrequest_404_response(self):
        response = self.client.get('/emergency/fireblock/incidents/?lat=-8d0.6875419&lon=4d0.032249')
        assert response.status_code == 404
    def test_fireblockincidents_404_response(self):
        response = self.client.get('/emergency/fireblock/incidents/?lat=-80.6875419&lon=40.032249')
        assert response.status_code == 404

class FMAEndpointsCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_200_response(self):
        response = self.client.get('/emergency/fmas/')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/emergency/fmas/23/')
        assert response.status_code == 200
    def geofilter_query_200_response(self):
        response = self.client.get('/emergency/fma/?lat=45.520697&lon=-122.677345')
        assert response.status_code == 200
    def test_404_response(self):
        response = self.client.get('/emergency/fma/?lat=-80.6875419&lon=40.032249')
        assert response.status_code == 404
    def test_geofilter_400_response(self):
        response = self.client.get('/emergency/fma/')
        assert response.status_code == 400
    def test_geofilter_404_response(self):
        response = self.client.get('/emergency/fma/?lat=-80.6875419&lon=40.032249')
        assert response.status_code == 404
    def fmaincidents_query_200_response(self):
        response = self.client.get('/emergency/fma/incidents/?lat=45.520697&lon=-122.677345')
        assert response.status_code == 200
    def test_fmaincidents_400_response(self):
        response = self.client.get('/emergency/fma/incidents/')
        assert response.status_code == 400
    def test_fireblockincidents_badrequest_404_response(self):
        response = self.client.get('/emergency/fireblock/incidents/?lat=-8d0.6875419&lon=4d0.032249')
        assert response.status_code == 404
    def test_fireblockincidents_404_response(self):
        response = self.client.get('/emergency/fireblock/incidents/?lat=-80.6875419&lon=40.032249')
        assert response.status_code == 404

class IncidentInfoEndpointCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_200_response(self):
        response = self.client.get('/emergency/incidents/info/?incident_id=1281359')
        assert response.status_code == 200
    def test_400_response(self):
        response = self.client.get('/emergency/incidents/info/')
        assert response.status_code == 400
    def test_404_bad_incident_id_response(self):
        response = self.client.get('/emergency/incidents/info/?incident_id=ab343')
        assert response.status_code == 404
    def test_404_not_found_incident_id_response(self):
        response = self.client.get('/emergency/incidents/info/?incident_id=564343')
        assert response.status_code == 404
