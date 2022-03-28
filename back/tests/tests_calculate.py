from unittest import TestCase

from api.services import calculate


class CalculateTests(TestCase):
    def test_add(self):
        self.assertEqual(calculate.add([4, 2]), 6)

    def test_subtract(self):
        self.assertEqual(calculate.subtract([4, 2]), 2)

    def test_multiply(self):
        self.assertEqual(calculate.multiply([4, 2]), 8)

    def test_divide(self):
        self.assertEqual(calculate.divide([4, 2]), 2)
