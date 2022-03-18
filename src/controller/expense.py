from src.service import expense as expense_service


def create_expense(payer_id, amount, user_ids, split_type, rem_input, app_variables):
    return expense_service.create_expense(payer_id, amount, user_ids, split_type, rem_input, app_variables)
