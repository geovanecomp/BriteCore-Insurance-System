from django.test import TestCase
from ..models import FieldType

class FieldTypeTestCase(TestCase):
    """ Test module for FieldType model """

    def setUp(self):
        FieldType.objects.create(name='test_name')

    def test_field_types_should_have_attr_name(self):
        """All field types must have the name attribute"""

        field_type = FieldType.objects.get(name='test_name')

        # TODO: Discover how to check if an attribute exists
        self.assertTrue(field_type.name == 'test_name')

    def test_field_type_name(self):
        """The field type should has the same inserted name"""

        field_type = FieldType.objects.get(name='test_name')

        self.assertEqual(field_type.name, 'test_name')
