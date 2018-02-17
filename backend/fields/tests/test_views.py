from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Field
from ..serializer import FieldSerializer
from field_types.models import FieldType
import json

client = Client()

def get_valid_object():
    valid_object = {
        'field_type': FieldType.objects.create(name='textfield'),
        # 'field_type_id': FieldType.objects.create(name='textfield').id,
        'label':'Test Field1',
        'description':'Desc test1',
        'required': False
    }
    return valid_object

def get_invalid_object():
    invalid_object = {
        'field_type': '',
        'label':'',
        'description':'',
        'required': ''
    }
    return invalid_object

class GetAllFields(TestCase):
    """ Test module for GET all fields API """

    def setUp(self):
        Field.objects.create(**get_valid_object())

    def test_get_all_fields(self):
        # get API response
        response = client.get(reverse('field-list'))

        # get data from db
        fields = Field.objects.all()
        serializer = FieldSerializer(fields, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleFieldTest(TestCase):
    """ Test module for GET single field API """

    def setUp(self):
        self.field1 = Field.objects.create(**get_valid_object())
        self.field2 = Field.objects.create(**get_valid_object())

    def test_get_valid_single_field(self):
        response = client.get(
            reverse('field-detail',  kwargs={'pk': self.field1.pk}))

        field = Field.objects.get(pk=self.field1.pk)
        serializer = FieldSerializer(field)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field(self):
        invalid_id = 999
        response = client.get(
            reverse('field-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewFieldTest(TestCase):
    """ Test module for inserting a new field """

    def setUp(self):
        self.valid_field = {
            'field_type': FieldType.objects.create(name='textfield').id,
            'label':'Test Field1',
            'description':'Desc test1',
            'required': False
        }

        self.invalid_field =  get_invalid_object()

    def test_create_valid_field(self):
        response = client.post(
            reverse('field-list'),
            data=json.dumps(self.valid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_field(self):
        response = client.post(
            reverse('field-list'),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleFieldTest(TestCase):
    """ Test module for update a single field """

    def setUp(self):
        self.field = Field.objects.create(**get_valid_object())

        self.valid_field = {
            'field_type': FieldType.objects.create(name='textfield').id,
            'label':'Test Field1',
            'description':'Desc test1',
            'required': False
        }

        self.invalid_field =  get_invalid_object()

    def test_update_valid_field(self):
        response = client.put(
            reverse('field-detail', kwargs={'pk': self.field.pk}),
            data=json.dumps(self.valid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_field(self):
        response = client.put(
            reverse('field-detail', kwargs={'pk': self.field.pk}),
            data=json.dumps(self.invalid_field),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleField(TestCase):
    """ Test module for deleting an existing field record """

    def setUp(self):
        self.field1 = Field.objects.create(**get_valid_object())
        self.field2 = Field.objects.create(**get_valid_object())

    def test_delete_valid_single_field(self):
        response = client.delete(
            reverse('field-detail',  kwargs={'pk': self.field1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field(self):
        invalid_id = 999
        response = client.delete(
            reverse('field-detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
