from src.model import user as user_model


def create_user(name, email, phone_number):
    return user_model.User(name, email, phone_number)

