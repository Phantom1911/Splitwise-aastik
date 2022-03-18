from src.model import transaction as transaction_model


def create_transaction(lender, borrower, amount):
    return transaction_model.Transaction(lender, borrower, amount)


def create_transactions(user_share_map, sample_users):
    # for user_id, share in user_share_map.items():
    #     user = list(filter(lambda x: x == user_id, sample_users))[0]
    pass

