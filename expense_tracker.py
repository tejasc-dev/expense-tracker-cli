import json
import argparse


class Expense:
    def __init__(self, date, description, amount,category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
        "date": self.date,
        "description": self.description,
        "amount": self.amount,
        "category": self.category
         }


    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                data["date"],
                data["description"],
                data["amount"],
                data.get("category", "uncategorized")
            )
        except (KeyError, TypeError):
            return None



class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 1 <= index <= len(self.expenses):
            del self.expenses[index - 1]
        else:
            print("Invalid index")

    def view_expenses(self):
        if not self.expenses:
            print("List is empty")
        else:
            for i, expense in enumerate(self.expenses, start=1):
                print(
                f"{i}. Date: {expense.date}, "
                f"Description: {expense.description}, "
                f"Amount: {expense.amount}, "
                f"Category: {expense.category}"
                                    )


    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses = ${total:.2f}")

    def save_to_file(self, filename="expenses.json"):
        data = [expense.to_dict() for expense in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    expense = Expense.from_dict(item)
                    if expense:
                        self.expenses.append(expense)
        except FileNotFoundError:
            pass


def main():
    tracker = ExpenseTracker()
    tracker.load_from_file()

    parser = argparse.ArgumentParser(
        description="Personal Expense Tracker CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--desc", required=True)
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", required=True)


    subparsers.add_parser("view", help="View all expenses")

    remove_parser = subparsers.add_parser("remove", help="Remove an expense")
    remove_parser.add_argument("--index", type=int, required=True)

    subparsers.add_parser("total", help="Show total expenses")

    args = parser.parse_args()

    if args.command == "add":
        tracker.add_expense(
            Expense(args.date, args.desc, args.amount,args.category)
        )
        tracker.save_to_file()
        print("Expense added")

    elif args.command == "view":
        tracker.view_expenses()

    elif args.command == "remove":
        tracker.remove_expense(args.index)
        tracker.save_to_file()
        print("Expense removed")

    elif args.command == "total":
        tracker.total_expenses()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
