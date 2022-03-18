import unittest
from src.service import expense as expense_service
from src.constants import split_type as split_type_constant
import initialise_script


splitwise_instance = initialise_script.initialise_app()
sample_users = splitwise_instance.users
payer_id = next(iter(sample_users))
user_ids = list(sample_users.keys())


def call_expense_service_to_create_expense(payer_user_id,
                                           total_amount,
                                           split_type,
                                           rem_input,
                                           ):
    return expense_service.create_expense(
        payer_user_id, total_amount, user_ids, split_type, rem_input, splitwise_instance)


class TestExpenseService(unittest.TestCase):
    def test_create_expense_with_equal_split(self):
        total_amount = 200
        split_type = split_type_constant['EQUAL']
        rem_input = []
        result = call_expense_service_to_create_expense(
            payer_id, total_amount, split_type, rem_input)
        updated_splitwise = result['updated_splitwise_instance']
        expense_map = updated_splitwise.get_expenses()
        user_expense = expense_map.get(payer_id)
        self.assertEqual(len(user_expense), 1)
        expense_obj = user_expense[0]
        self.assertEqual(expense_obj.user.get_id(), payer_id)

        split_obj = expense_obj.split
        expected_share = {}
        for u_id in user_ids:
            expected_share[u_id] = 50

        self.assertEqual(split_obj.get_share(), expected_share)

        self.assertEqual(split_obj.type, split_type_constant['EQUAL'])

    def test_create_expense_with_percent_split(self):
        total_amount = 143.13
        split_type = split_type_constant['PERCENT']
        share_input = [20, 30, 20, 30]
        result = call_expense_service_to_create_expense(
            payer_id,
            total_amount,
            split_type,
            share_input)

        updated_splitwise_obj = result['updated_splitwise_instance']
        expense_map = updated_splitwise_obj.get_expenses()
        user_expense = expense_map.get(payer_id)
        self.assertEqual(len(user_expense), 2)
        expense_obj = user_expense[1]
        split_obj = expense_obj.split
        expected_share = {}
        num_users = len(user_ids)
        share_div = [28.63, 42.94, 28.63, 42.94]
        for i in range(num_users):
            expected_share[user_ids[i]] = share_div[i]

        self.assertEqual(split_obj.get_share(), expected_share)
        self.assertEqual(split_obj.type, split_type_constant['PERCENT'])
        self.assertEqual(expense_obj.amount, 143.13)