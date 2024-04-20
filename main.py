from ex import Expense
import datetime
import calendar

def main():
    print("Expense tracker is running")
    expense_file_path = "expense.csv"
    budget = 2000000

    expense = expense_kitna_hua()

    file_m_save(expense, expense_file_path)

    summarize_expenses(expense_file_path, budget)


def expense_kitna_hua():
    print("Enter your expense details")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("Select expense category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter category number ({value_range}): ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            print(f"Selected category: {selected_category}")

            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category number")


def file_m_save(expense: Expense, expense_file_path):
    print(f"Saving expense to file: {expense} -> {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def summarize_expenses(expense_file_path, budget):
    print("Summary of user expenses")
    expenses = []  # Initialize expenses list
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")  # Split line by comma
            print(f"{expense_name}, {expense_amount}, {expense_category}")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)  # Append expense to expenses list

    amount_by_category = {}
    for exp in expenses:
        key = exp.category
        if key in amount_by_category:
            amount_by_category[key] += exp.amount
        else:
            amount_by_category[key] = exp.amount

    print("Category-wise expenses:")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount}")

    total_spent = sum(exp.amount for exp in expenses)
    print(f"Total spent: {total_spent}")

    remaining_budget = budget - total_spent
    print(f"Remaining budget: {remaining_budget}")

    now = datetime.datetime.now()
    day_in_month = calendar.monthrange(now.year, now.month)[1]  # Get the number of days in the current month
    remaining_days = day_in_month - now.day
    print(f"Remaining days in the month: {remaining_days}")

    daily_budget = remaining_budget / remaining_days
    print(red(f"Daily budget: {daily_budget}"))

def red(text):
    return f"\033[91m{text}\033[0m"

if __name__ == "__main__":
    main()
