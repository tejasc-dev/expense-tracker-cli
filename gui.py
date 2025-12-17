import tkinter as tk
from database import init_db
from tracker import ExpenseTracker,Expense

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")

init_db()
tracker = ExpenseTracker()
print("fetch_all exists:", hasattr(tracker, "fetch_all"))


tk.Label(root, text="Date").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Description").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

def add_expense():
    try:
        expense = Expense(
            date_entry.get(),
            desc_entry.get(),
            float(amount_entry.get()),
            category_entry.get()
        )
        tracker.add_expense(expense)
        status_label.config(text="Expense added")
    except ValueError:
        status_label.config(text="Amount must be a number")

tk.Button(root, text="Add Expense", command=add_expense).pack()
status_label = tk.Label(root, text="")
status_label.pack()

listbox = tk.Listbox(root,width=60)
listbox.pack()

def refresh_expenses():
    listbox.delete(0, tk.END)
    for row in tracker.fetch_all():
        listbox.insert(
            tk.END,
            f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}"
        )

tk.Button(root, text="View Expenses", command=refresh_expenses).pack()

def show_category_totals():
    listbox.delete(0, tk.END)
    rows = tracker.category_totals()

    if not rows:
        listbox.insert(tk.END, "No expenses found")
        return

    for cat, total in rows:
        listbox.insert(tk.END, f"{cat}: ₹{total:.2f}")


tk.Button(root, text="Category Summary", command=show_category_totals).pack()

root.mainloop()