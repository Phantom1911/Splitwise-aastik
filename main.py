import initialise_script
from src.constants import valid_actions
from src.action import execute

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Splitwise Application', '\n')
    splitwise_instance = initialise_script.initialise_app()

    print('Available user ids:')

    print(list(splitwise_instance.users.keys()))
    print('\n')
    print('Available commands:')

    for key, value in valid_actions.items():
        print(value, end=', ')
    print('\n')
    print('type EXIT to stop the application')
    equal_splitter = factory.get('equal;')
    while True:
        user_input = input('Enter command:')
        if user_input.upper() == valid_actions['EXIT']:
            break
        result = execute(user_input.split(' '), splitwise_instance)
        if result != None:
            print(result)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
