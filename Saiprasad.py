import json
import os

def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def add_income(data):
    while True:
        try:
            income = float(input("Enter income amount: "))
            if income <= 0:
                print("Income amount must be a positive number.")
                continue
            data["income"] += income
            print("Income added successfully!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for income.")

def add_expense(data):
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Expense amount must be a positive number.")
                continue
            category = input("Enter expense category: ").strip()
            if not category:
                print("Category cannot be empty.")
                continue
            data["expenses"].append({"amount": amount, "category": category})
            print("Expense added successfully!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.")

def calculate_budget(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    budget = data["income"] - total_expenses
    return budget

def analyze_expenses(data):
    expense_categories = {}
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category]["amount"] += amount
            expense_categories[category]["percentage"] = (expense_categories[category]["amount"] / total_expenses) * 100
        else:
            expense_categories[category] = {"amount": amount, "percentage": (amount / total_expenses) * 100}
    return expense_categories

def main():
    data = load_data()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            budget = calculate_budget(data)
            print(f"Your remaining budget is: {budget}")
        elif choice == "4":
            expense_analysis = analyze_expenses(data)
            print("Expense Analysis:")
            for category, info in expense_analysis.items():
                print(f"{category}: {info['amount']} ({info['percentage']:.2f}%)")
        elif choice == "5":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main ()
