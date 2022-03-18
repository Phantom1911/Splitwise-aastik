
class Splitwise:
    def __init__(self, users):
        self.users = users
        # expenses is a map , user_id : expense
        self._expenses = {}

    def set_expense(self, expense):
        user_id = expense.user.get_id()
        user_expense = self._expenses.get(user_id, None)
        if user_expense:
            self._expenses[user_id].append(expense)
        else:
            self._expenses[user_id] = [expense]

    def get_expenses(self):
        return self._expenses

