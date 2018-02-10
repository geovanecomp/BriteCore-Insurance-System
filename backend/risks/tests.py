from django.test import TestCase
from .models import RiskType

class RiskTypeTestCase(TestCase):
    def setUp(self):
        RiskType.objects.create(name='test_name')

    def test_risk_types_should_have_name(self):
        """All risk types must have the name attribute"""

        risk_type = RiskType.objects.get(name='test_name')

        self.assertTrue(risk_type.name == 'test_name')
