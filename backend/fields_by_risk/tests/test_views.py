from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..serializer import FieldByRiskSerializer
from ..models import FieldByRisk
from fields.models import Field
from field_types.models import FieldType
from risks.models import Risk
from risk_types.models import RiskType

import json

client = Client()

def get_valid_object():
    field_type = FieldType.objects.create(name='Test Field Type')
    field = Field.objects.create(label='Test Field', field_type=field_type, required=False)

    risk_type = RiskType.objects.create(name='Test Risk Type')
    risk = Risk.objects.create(name='Test Risk', risk_type=risk_type)

    valid_object = {
        'field': field,
        'risk': risk
    }

    return valid_object

def get_invalid_object():
    invalid_object = {
        'field': '',
        'risk': ''
    }

    return invalid_object

class GetAllFieldsByRisk(TestCase):
    """ Test module for GET all fields by risk API """

    def setUp(self):
        FieldByRisk.objects.create(**get_valid_object())

    def test_get_all_fields(self):
        # get API response
        response = client.get(reverse('fieldbyrisk-list'))

        # get data from db
        fields_by_risk = FieldByRisk.objects.all()
        serializer = FieldByRiskSerializer(fields_by_risk, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_fields_by_risk(self):
        risk_id = 1

        # Get API response
        response = client.get(reverse('fieldbyrisk-list-fields-by-risk'), {'risk_id': risk_id})

        # get data from db
        fields_by_risk = FieldByRisk.objects.filter(risk_id=risk_id)

        serializer = FieldByRiskSerializer(fields_by_risk, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleFieldByRiskTest(TestCase):
    """ Test module for GET single field API """

    def setUp(self):
        self.fields_by_risk = FieldByRisk.objects.create(**get_valid_object())

    def test_get_valid_single_field(self):
        response = client.get(
            reverse('fieldbyrisk-detail',  kwargs={'pk': self.fields_by_risk.pk}))

        field = FieldByRisk.objects.get(pk=self.fields_by_risk.pk)
        serializer = FieldByRiskSerializer(field)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field(self):
        invalid_id = 999
        response = client.get(
            reverse('fieldbyrisk-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewFieldByRiskTest(TestCase):
    """ Test module for inserting a new field """

    def setUp(self):
        field_type = FieldType.objects.create(name='Test Field Type')
        field = Field.objects.create(label='Test Field', field_type=field_type, required=False).id

        risk_type = RiskType.objects.create(name='Test Risk Type')
        risk = Risk.objects.create(name='Test Risk', risk_type=risk_type).id

        self.valid_field = {
            'field': field,
            'risk': risk,
            'value': 'Test value'
        }

        self.invalid_field =  get_invalid_object()
    
    def test_create_invalid_field(self):
        response = client.post(
            reverse('fieldbyrisk-list'),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleFieldByRiskTest(TestCase):
    """ Test module for update a single field """

    def setUp(self):
        self.field_by_risk = FieldByRisk.objects.create(**get_valid_object())

        field_type = FieldType.objects.create(name='Test Field Type')
        field = Field.objects.create(label='Test Field', field_type=field_type, required=False).id

        risk_type = RiskType.objects.create(name='Test Risk Type')
        risk = Risk.objects.create(name='Test Risk', risk_type=risk_type).id

        self.valid_field = {
            'field': field,
            'risk': risk,
            'value': 'Test value'

        }

        self.invalid_field =  get_invalid_object()

    def test_update_valid_field(self):
        response = client.put(
            reverse('fieldbyrisk-detail', kwargs={'pk': self.field_by_risk.pk}),
            data=json.dumps(self.valid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_field(self):
        response = client.put(
            reverse('fieldbyrisk-detail', kwargs={'pk': self.field_by_risk.pk}),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleField(TestCase):
    """ Test module for deleting an existing field record """

    def setUp(self):
        self.field1 = FieldByRisk.objects.create(**get_valid_object())
        self.field2 = FieldByRisk.objects.create(**get_valid_object())

    def test_delete_valid_single_field(self):
        response = client.delete(
            reverse('fieldbyrisk-detail',  kwargs={'pk': self.field1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field(self):
        invalid_id = 999
        response = client.delete(
            reverse('fieldbyrisk-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
