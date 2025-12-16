# Expense Tracker CLI

A simple command-line expense tracker built in Python to record, view, and manage personal expenses.  
The focus of this project is clean object-oriented design, persistence using JSON, and practical CLI usage.

## Features
- Add expenses with date, description, amount, and category
- View all recorded expenses
- Remove expenses by index
- Calculate total expenses
- Persist data automatically using a JSON file
- Simple and intuitive CLI interface using `argparse`

## Tech Stack
- Python
- argparse
- JSON (for persistence)

## Usage

### Add an expense
```bash
python expense_tracker.py add --date 2025-01-10 --desc "Groceries" --amount 450 --category Food
