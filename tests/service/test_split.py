from src.service import split as split_service
from src.constants import split_type as split_type_constant, output_messages
import unittest


total_amount = 143.13
user_ids = [1, 2, 3]


class TestSplitService(unittest.TestCase):
    def test_create_split_instance(self):
        share_div = [47.71, 47.71, 47.71]
        split_obj = split_service.create_split_instance(split_type_constant['EQUAL'], user_ids, share_div)
        self.assertEqual(split_obj.type, split_type_constant['EQUAL'])
        expected_share_map = {
            1: 47.71,
            2: 47.71,
            3: 47.71
        }
        self.assertEqual(split_obj.get_share(), expected_share_map)

    def test_create_equal_split(self):
        no_of_users = 3
        split_obj = split_service.create_equal_split(total_amount, [no_of_users], user_ids)
        self.assertEqual(split_obj.type, split_type_constant['EQUAL'])
        expected_share_map = {
            1: 47.71,
            2: 47.71,
            3: 47.71
        }
        self.assertEqual(split_obj.get_share(), expected_share_map)

    def test_create_percent_split(self):
        percent = [20, 30, 50]
        split_obj = split_service.create_percent_split(total_amount, percent, user_ids)

        self.assertEqual(split_obj.type, split_type_constant['PERCENT'])
        expected_share_div = {
            1: 28.63,
            2: 42.94,
            3: 71.56
        }
        self.assertEqual(split_obj.get_share(), expected_share_div)

    def test_create_exact_split(self):
        exact = [28.63, 42.94, 71.56]
        split_obj = split_service.create_exact_split(total_amount, exact, user_ids)
        self.assertEqual(split_obj.type, split_type_constant['EXACT'])
        expected_share_div = {
            1: 28.63,
            2: 42.94,
            3: 71.56
        }
        self.assertEqual(split_obj.get_share(), expected_share_div)

    def test_create_percent_split_fail(self):
        percent = [20, 30, 20]
        result = split_service.create_percent_split(total_amount, percent, user_ids)
        self.assertEqual(result['err_msg'], output_messages['INVALID_PERCENT_SPLIT'])

    def test_create_exact_split_fail(self):
        exact = [28.63, 42.94, 90.56]
        result = split_service.create_exact_split(total_amount, exact, user_ids)
        self.assertEqual(result['err_msg'], output_messages['INVALID_EXACT_SPLIT'])
