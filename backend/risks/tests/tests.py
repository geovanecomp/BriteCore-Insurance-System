from django.test import TestCase
from ..models import RiskType

class RiskTypeTestCase(TestCase):
    """ Test module for RiskType model """

    def setUp(self):
        RiskType.objects.create(name='test_name')

    def test_risk_types_should_have_attr_name(self):
        """All risk types must have the name attribute"""

        risk_type = RiskType.objects.get(name='test_name')

        # TODO: Discover how to check if an attribute exists
        self.assertTrue(risk_type.name == 'test_name')

    def test_risk_type_name(self):
        """The risk type should has the same inserted name"""

        risk_type = RiskType.objects.get(name='test_name')

        self.assertEqual(risk_type.name, 'test_name')
