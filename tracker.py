from database import get_connection

class Expense:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category


class ExpenseTracker:
    def add_expense(self, expense):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)",
            (expense.date, expense.description, expense.amount, expense.category)
        )

        conn.commit()
        conn.close()

    def fetch_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, date, description, amount, category FROM expenses"
        )
        rows = cursor.fetchall()
        conn.close()
        return rows

    def category_totals(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)

        rows = cursor.fetchall()
        conn.close()
        return rows

    def total_expenses(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT SUM(amount) FROM expenses")
        total = cursor.fetchone()[0] or 0
        conn.close()
        return total
