import unittest
from src.service import user as user_service


class TestUserService(unittest.TestCase):
    def test_create_user(self):
        name = 'Ross Geller'
        email = 'ross.geller@gmail.com'
        number = '1234567890'
        user = user_service.create_user(name, email, number)
        self.assertEqual(user.name, 'Ross Geller')
        self.assertEqual(user.email, 'ross.geller@gmail.com')