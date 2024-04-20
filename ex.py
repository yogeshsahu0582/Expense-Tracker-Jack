class Expense:
    def __init__(self, category, amount, name):
        self.category = category
        self.amount = amount
        self.name = name
    def __repr__(self):
        return f"Expense:{self.name} {self.category}{self.amount:.2f}"

