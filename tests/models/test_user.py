import unittest
from src.model import user as user_model


class TestUserModel(unittest.TestCase):
    def test_user_init(self):
        name = 'Ross Geller'
        email = 'ross.geller@gmail.com'
        number = '1234567890'
        user = user_model.User(name, email, number)
        self.assertEqual(user.name, 'Ross Geller')
        self.assertEqual(user.email, 'ross.geller@gmail.com')



if __name__ == '__main__':
    unittest.main()