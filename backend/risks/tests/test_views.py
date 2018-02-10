from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import RiskType
from ..serializer import RiskTypeSerializer
import json
client = Client()

class GetAllRiskTypes(TestCase):
    """ Test module for GET all risk types API """

    def setUp(self):
        RiskType.objects.create(name='Test Risk1')
        RiskType.objects.create(name='Test Risk2')

    def test_get_all_risk_types(self):
        # get API response
        response = client.get(reverse('get_post_risk_type'))

        # get data from db
        risk_types = RiskType.objects.all()
        serializer = RiskTypeSerializer(risk_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTypeTest(TestCase):
    """ Test module for GET single risk type API """

    def setUp(self):
        self.risk_type1 = RiskType.objects.create(name='Test Risk1')
        self.risk_type2 = RiskType.objects.create(name='Test Risk2')

    def test_get_valid_single_risk_type(self):
        response = client.get(
            reverse('get_delete_update_risk_type',  kwargs={'pk': self.risk_type1.pk}))

        risk = RiskType.objects.get(pk=self.risk_type1.pk)
        serializer = RiskTypeSerializer(risk)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk_type(self):
        invalid_id = 999
        response = client.get(
            reverse('get_delete_update_risk_type',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewRiskTypeTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_risk_type = {
            'name': 'Test Risk'
        }

        self.invalid_risk_type =  {
            'name': ''
        }

    def test_create_valid_risk_type(self):
        response = client.post(
            reverse('get_post_risk_type'),
            data=json.dumps(self.valid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk_type(self):
        response = client.post(
            reverse('get_post_risk_type'),
            data=json.dumps(self.invalid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
