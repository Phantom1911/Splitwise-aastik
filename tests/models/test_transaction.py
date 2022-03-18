
import unittest
from src.model import transaction as transaction_model, user as user_model


class TestUserModel(unittest.TestCase):
    def test_user_init(self):
        payer = user_model.User('Ross', 'ross.geller@gmail.com', '1234567890')
        receiver = user_model.User('Chandler', 'chandler@gmail.com', '1231231231')
        transaction = transaction_model.Transaction(payer, receiver, 50)
        self.assertEqual(transaction.amount, 50)


if __name__ == '__main__':
    unittest.main()
