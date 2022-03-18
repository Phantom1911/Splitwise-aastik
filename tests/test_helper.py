from src.helper import share as share_helper
import unittest


class TestHelper(unittest.TestCase):
    def test_divide_amount_in_equal_share(self):
        total_amount = 143.13
        divider = 5
        share_division = share_helper.divide_amount_in_equal_share(total_amount, divider)
        self.assertEqual(share_division, [28.63, 28.62, 28.63, 28.62, 28.63])

    def test_divide_amount_by_percent_share(self):
        total_amount = 143.13
        percent = [20, 30, 50]
        share_div = share_helper.divide_amount_by_percent_share(total_amount, percent)
        expected_share_div = [28.63, 42.94, 71.56]
        self.assertEqual(share_div, expected_share_div)

    # def test_divide_amount_by_exact_share(self):
    #     total_amount = 143.13
    #     exact_share = [28.63, 42.94, 71.56]

