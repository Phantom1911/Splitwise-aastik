import uuid


class User:
    def __init__(self, id, name, email, phone_number):
        self._id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        # friends in an object with user and amount
        self.friends = {}

    def get_id(self):
        return self._id
