import unittest
from src.model import split as split_model, user as user_model
from src.constants import split_type as split_type_constant

split_type = split_type_constant['EQUAL']


class SplitModel(unittest.TestCase):
    def test_split_init(self):
        split = split_model.Split(split_type)
        self.assertEqual(split.type, split_type)

    def test_split_set_up(self):
        user1 = user_model.User('Sherlock', 'sherlock@gmail.com', '1231231231')
        user2 = user_model.User('Brewstorm', 'brewstorm@gmail.com', '1231231231')
        split = split_model.Split(split_type)
        share = {user1.get_id(): 130, user2.get_id(): 130}
        split.set_share(share)
        newly_added_share = split.get_share()
        self.assertEqual(newly_added_share, share)


if __name__ == '__main__':
    unittest.main()

