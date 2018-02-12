from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Risk
from ..serializer import RiskSerializer
from risk_types.models import RiskType
import json

client = Client()

def get_valid_object():
    valid_object = {
        'risk_type': RiskType.objects.create(name='textfield'),
        'name':'Test Risk1',
        'description':'Desc test1'
    }
    return valid_object

def get_invalid_object():
    invalid_object = {
        'risk_type': '',
        'name':'',
        'description':''
    }
    return invalid_object

class GetAllRisks(TestCase):
    """ Test module for GET all risks API """

    def setUp(self):
        Risk.objects.create(**get_valid_object())

    def test_get_all_risks(self):
        # get API response
        response = client.get(reverse('risk-list'))

        # get data from db
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTest(TestCase):
    """ Test module for GET single field API """

    def setUp(self):
        self.field1 = Risk.objects.create(**get_valid_object())
        self.field2 = Risk.objects.create(**get_valid_object())

    def test_get_valid_single_field(self):
        response = client.get(
            reverse('risk-detail',  kwargs={'pk': self.field1.pk}))

        field = Risk.objects.get(pk=self.field1.pk)
        serializer = RiskSerializer(field)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field(self):
        invalid_id = 999
        response = client.get(
            reverse('risk-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewRiskTest(TestCase):
    """ Test module for inserting a new field """

    def setUp(self):
        self.valid_field = {
            'risk_type': RiskType.objects.create(name='textfield').id,
            'name':'Test Risk1',
            'description':'Desc test1'
        }

        self.invalid_field =  get_invalid_object()

    def test_create_valid_field(self):
        response = client.post(
            reverse('risk-list'),
            data=json.dumps(self.valid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_field(self):
        response = client.post(
            reverse('risk-list'),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleRiskTest(TestCase):
    """ Test module for update a single field """

    def setUp(self):
        self.field = Risk.objects.create(**get_valid_object())

        self.valid_field = {
            'risk_type': RiskType.objects.create(name='textfield').id,
            'name':'Test Risk1',
            'description':'Desc test1'
        }

        self.invalid_field =  get_invalid_object()

    def test_update_valid_field(self):
        response = client.put(
            reverse('risk-detail', kwargs={'pk': self.field.pk}),
            data=json.dumps(self.valid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_field(self):
        response = client.put(
            reverse('risk-detail', kwargs={'pk': self.field.pk}),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRisk(TestCase):
    """ Test module for deleting an existing field record """

    def setUp(self):
        self.field1 = Risk.objects.create(**get_valid_object())
        self.field2 = Risk.objects.create(**get_valid_object())

    def test_delete_valid_single_field(self):
        response = client.delete(
            reverse('risk-detail',  kwargs={'pk': self.field1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field(self):
        invalid_id = 999
        response = client.delete(
            reverse('risk-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
