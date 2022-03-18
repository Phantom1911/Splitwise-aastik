from src.model import expense as expense_model
from src.service import split as split_service
from src.constants import output_messages


def create_expense(payer_id, amount, user_ids, split_type, rem_input, splitwise_instance):
    sample_users = splitwise_instance.users
    if len(rem_input) > 0:
        share_unit = rem_input   # share_unit = [370,880]
    else:
        # no rem input means equal split
        # equal split, send num of users
        share_unit = [len(user_ids)]   # share_unit = [4]
    payer = sample_users.get(payer_id, None)
    if not payer:
        return {
            'err_msg': output_messages['INVALID_USER_ID']
        }
    # split_obj is type of split and share , where share is map of user_id to share in that particular split
    split_obj = split_service.create_split(split_type, amount, share_unit, user_ids)
    expense_obj = expense_model.Expense(payer, amount, split_obj)
    splitwise_instance.set_expense(expense_obj)
    return {
        'success_msg': 'Successfully added expense',
        'updated_splitwise_instance': splitwise_instance
    }

