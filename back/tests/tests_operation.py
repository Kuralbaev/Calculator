from unittest import TestCase

from api.services import calculate
from api.services.Operator import Operator


class OperationTests(TestCase):
    def test_operation_add(self):
        self.assertEqual(Operator('+').operation, calculate.add)

    def test_operation_subtract(self):
        self.assertEqual(Operator('-').operation, calculate.subtract)

    def test_operation_multiply(self):
        self.assertEqual(Operator('*').operation, calculate.multiply)

    def test_operation_divide(self):
        self.assertEqual(Operator('/').operation, calculate.divide)
