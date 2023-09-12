from django.test import TestCase
from store.logic import calculator


class LogicTestCase(TestCase):
    def test_plus(self):
        result = calculator(3, 6, '+')
        self.assertEqual(9, result)
