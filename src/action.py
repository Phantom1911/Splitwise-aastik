# add expense: u1 1200 4 u1 u2 u3 u4 exact 1000 20 30 150
# settle up u1 u2 300

from src.controller import expense as expense_controller
from src.validation import is_action_valid
from src.constants import output_messages, valid_actions


def process_expense_addition_input(input_cmd):
    payer_id = input_cmd[0]
    amount = int(input_cmd[1])
    number_of_users_involved = int(input_cmd[2])
    user_ids = []
    for idx in range(number_of_users_involved):
        u_id = input_cmd[3 + idx]
        user_ids.append(u_id)
    cur_idx = 2 + number_of_users_involved + 1
    split_type = input_cmd[cur_idx]
    return payer_id, amount, user_ids, split_type, cur_idx


def execute_expense_addition(input_list, splitwise_instance):
    payer_id, amount, user_ids, split_type, current_idx = process_expense_addition_input(input_list)
    if current_idx == len(input_list) - 1:
        rem_input = []
    else:
        rem_input = input_list[current_idx+1:]
        rem_input = [int(i) for i in rem_input]
    execution_result = expense_controller.create_expense(
        payer_id, amount, user_ids, split_type, rem_input, splitwise_instance)
    return execution_result

def execute_show_balance(user_id, splitwise_instance):
    if len(splitwise_instance._expenses) == 0:
        print("No balance")
        return
    if user_id is None:
        all_users = splitwise_instance.users
        for u in all_users:
            show_balance(u, splitwise_instance)
    else:
        show_balance(user_id, splitwise_instance)

def show_balance(user_id, splitwise_instance):
    owings_to_curr_user = {}
    if user_id not in splitwise_instance._expenses:
        print(f"no payment made by {user_id} yet, nobody owes him anything")
        return
    current_user_expenses = splitwise_instance._expenses[user_id]
    for expense in current_user_expenses:
        share = expense.split._share
        for u in share:
            if u == user_id:
                continue
            if u not in owings_to_curr_user:
                owings_to_curr_user[u] = 0
            owings_to_curr_user[u] += share[u]

    for u in owings_to_curr_user:
        print(f"User {u} owes {user_id} " + str(owings_to_curr_user[u]))


def execute(user_input, splitwise_instance):
    action = user_input[0]
    if not is_action_valid(action):
        return {
            'error_message': output_messages['INVALID_ACTION']
        }

    if action.upper() == valid_actions['ADD_EXPENSE']:
        added_expense_result = execute_expense_addition(user_input[1:], splitwise_instance)

        return added_expense_result

    elif action.upper() == valid_actions['SHOW']:
        if len(user_input) == 1:
            user_id = None
        else:
            user_id = user_input[1]
        show_expense_result = execute_show_balance(user_id, splitwise_instance)
