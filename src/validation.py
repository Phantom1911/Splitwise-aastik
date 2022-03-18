from src.constants import split_type as split_type_constant, valid_actions


def is_split_type_valid(split_type):
    if split_type.upper() in split_type_constant.values():
        return True
    return False


def is_action_valid(action):
    if action.upper() in valid_actions.values():
        return True
    else:
        return False


def is_percent_share_valid(share_list, num_users):
    if len(share_list) != 0 and len(share_list) == num_users and sum(share_list) == 100:
        return True
    else:
        return False


def is_exact_share_valid(total, share_list, num_users):
    if len(share_list) == num_users and sum(share_list) == total:
        return True
    else:
        return False

# owings :  owed_by, owed_to, amount

# u1 -- u2 , u3, u4
# u2 -- u1, u3, u4
# {user : total_amount}
# {user1: {u2: 20, u3:50}}
#
# owings_list = []
# owings[idx] =