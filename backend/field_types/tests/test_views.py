from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import FieldType
from ..serializer import FieldTypeSerializer
import json
client = Client()

class GetAllFieldTypes(TestCase):
    """ Test module for GET all field types API """

    def setUp(self):
        FieldType.objects.create(name='Test Field1', description='Desc test1')
        FieldType.objects.create(name='Test Field2', description='Desc test1')

    def test_get_all_field_types(self):
        # get API response
        response = client.get(reverse('field_type'))

        # get data from db
        field_types = FieldType.objects.all()
        serializer = FieldTypeSerializer(field_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleFieldTypeTest(TestCase):
    """ Test module for GET single field type API """

    def setUp(self):
        self.field_type1 = FieldType.objects.create(name='Test Field1', description='Desc test1')
        self.field_type2 = FieldType.objects.create(name='Test Field2', description='Desc test12')

    def test_get_valid_single_field_type(self):
        response = client.get(
            reverse('field_type_detail',  kwargs={'pk': self.field_type1.pk}))

        field = FieldType.objects.get(pk=self.field_type1.pk)
        serializer = FieldTypeSerializer(field)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field_type(self):
        invalid_id = 999
        response = client.get(
            reverse('field_type_detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewFieldTypeTest(TestCase):
    """ Test module for inserting a new field type """

    def setUp(self):
        self.valid_field_type = {
            'name': 'Test Field',
            'description': 'Desc Field'
        }

        self.invalid_field_type =  {
            'name': '',
            'description': ''
        }

    def test_create_valid_field_type(self):
        response = client.post(
            reverse('field_type'),
            data=json.dumps(self.valid_field_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_field_type(self):
        response = client.post(
            reverse('field_type'),
            data=json.dumps(self.invalid_field_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleFieldTypeTest(TestCase):
    """ Test module for update a single field type """

    def setUp(self):
        self.field_type = FieldType.objects.create(name='Test Field1', description='Desc test')

        self.valid_field_type = {
            'name': 'Updated Test Field',
            'description': 'Test'
        }

        self.invalid_field_type =  {
            'name': '',
            'description': ''
        }

    def test_update_valid_field_type(self):
        response = client.put(
            reverse('field_type_detail', kwargs={'pk': self.field_type.pk}),
            data=json.dumps(self.valid_field_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_field_type(self):
        response = client.put(
            reverse('field_type_detail', kwargs={'pk': self.field_type.pk}),
            data=json.dumps(self.invalid_field_type),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFieldType(TestCase):
    """ Test module for deleting an existing field type record """

    def setUp(self):
        self.field_type1 = FieldType.objects.create(name='Test Field1')
        self.field_type2 = FieldType.objects.create(name='Test Field2')

    def test_delete_valid_single_field_type(self):
        response = client.delete(
            reverse('field_type_detail',  kwargs={'pk': self.field_type1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field_type(self):
        invalid_id = 999
        response = client.delete(
            reverse('field_type_detail',  kwargs={'pk': invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
