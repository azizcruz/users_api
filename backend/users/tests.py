from django.test import TestCase
from rest_framework.test import RequestsClient
from users.models import (
    FakeAddress,
    FakeCompany,
    FakeGeo,
    FakeUser
)

# Create your tests here.
class ApiTests(TestCase):
    def setUp(self):
        # Client to send test requests
        self.client = RequestsClient()

        # Dummy data to be tested
        self.user = FakeUser.objects.create(
            name = 'name for test',
            username = 'username for test',
            email = 'email for test',
            phone = '555566222',
            website = 'www.test.com'
        )

        self.address = FakeAddress.objects.create(
            user = self.user,
            street = 'street for test',
            suite = 'suite for test',
            city = 'city for test',
            zipcode = '4445'
        )

        self.geo = FakeGeo.objects.get_or_create(
            address = self.address,
            lat = '66561.235',
            lng = '23.354'
        )

        self.company = FakeCompany.objects.get_or_create(
            user = self.user,
            name = 'company name',
            catchPhrase = 'random phrase',
            bs = 'random bs'
        )

    def test_the_endpoint_returns_200(self):
        """
        Test if the enpoint is working and fetching data succefully
        """
        response = self.client.get('http://localhost:8000/users/')
        self.assertEqual(response.status_code, 200)

    def test_the_endpoint_returns_data(self):
        """
        Test if the enpoint is working and fetching data succefully
        """
        response = self.client.get('http://localhost:8000/users/')
        self.assertEqual(len(response.json()), 1)

