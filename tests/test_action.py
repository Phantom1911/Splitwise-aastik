from src.action import process_expense_addition_input
from src.constants import split_type as split_type_constant
import unittest


class TestAction(unittest.TestCase):
    def test_process_expense_addition_input(self):
        test_input = [1, 200, 3, 1, 2, 3, split_type_constant['EQUAL']]
        result = process_expense_addition_input(test_input)
        self.assertEqual(result[0], test_input[0])
        self.assertEqual(result[1], test_input[1])
        self.assertEqual(result[2], [1, 2, 3])
        self.assertEqual(result[3],  split_type_constant['EQUAL'])