from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import RiskType
from ..serializer import RiskTypeSerializer
import json
client = Client()

def get_valid_object():
    valid_object = {
        'name':'Test Risk',
        'description':'Desc test'
    }
    return valid_object

def get_invalid_object():
    valid_object = {
        'name':'',
        'description':''
    }
    return valid_object

class GetAllRiskTypes(TestCase):
    """ Test module for GET all risk types API """

    def setUp(self):
        RiskType.objects.create(**get_valid_object())
        RiskType.objects.create(**get_valid_object())

    def test_get_all_risk_types(self):
        # get API response
        response = client.get(reverse('risk_type'))

        # get data from db
        risk_types = RiskType.objects.all()
        serializer = RiskTypeSerializer(risk_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTypeTest(TestCase):
    """ Test module for GET single risk type API """

    def setUp(self):
        self.risk_type1 = RiskType.objects.create(**get_valid_object())
        self.risk_type2 = RiskType.objects.create(**get_valid_object())

    def test_get_valid_single_risk_type(self):
        response = client.get(
            reverse('risk_type_detail',  kwargs={'pk': self.risk_type1.pk}))

        risk = RiskType.objects.get(pk=self.risk_type1.pk)
        serializer = RiskTypeSerializer(risk)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk_type(self):
        invalid_id = 999
        response = client.get(
            reverse('risk_type_detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewRiskTypeTest(TestCase):
    """ Test module for inserting a new risk type """

    def setUp(self):
        self.valid_risk_type = get_valid_object()

        self.invalid_risk_type =  get_invalid_object()

    def test_create_valid_risk_type(self):
        response = client.post(
            reverse('risk_type'),
            data=json.dumps(self.valid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk_type(self):
        response = client.post(
            reverse('risk_type'),
            data=json.dumps(self.invalid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleRiskTypeTest(TestCase):
    """ Test module for update a single risk type """

    def setUp(self):
        self.risk_type = RiskType.objects.create(**get_valid_object())

        self.valid_risk_type = get_valid_object()

        self.invalid_risk_type =  get_invalid_object()

    def test_update_valid_risk_type(self):
        response = client.put(
            reverse('risk_type_detail', kwargs={'pk': self.risk_type.pk}),
            data=json.dumps(self.valid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_risk_type(self):
        response = client.put(
            reverse('risk_type_detail', kwargs={'pk': self.risk_type.pk}),
            data=json.dumps(self.invalid_risk_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRiskType(TestCase):
    """ Test module for deleting an existing risk type record """

    def setUp(self):
        self.risk_type1 = RiskType.objects.create(**get_valid_object())
        self.risk_type2 = RiskType.objects.create(**get_valid_object())

    def test_delete_valid_single_risk_type(self):
        response = client.delete(
            reverse('risk_type_detail',  kwargs={'pk': self.risk_type1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_risk_type(self):
        invalid_id = 999
        response = client.delete(
            reverse('risk_type_detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
