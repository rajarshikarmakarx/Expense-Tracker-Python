# Expense Tracker 💰

A simple command-line expense tracker built in Python. Log your daily expenses with a date, name, category, and amount, view them, edit or delete entries, and generate quick reports — all backed by a local CSV file.

## Features

- **Add new expense entries** — capture date, description, category, and amount
- **View existing entries** — print all saved expenses to the console in a formatted table, with a running total
- **Edit existing entries** — pick an expense by ID, choose a field (Date, Name, Category, or Amount), and update it with input validation
- **Delete existing entries** — pick an expense by ID, preview it, and confirm before removal
- **Reports**
  - Category-wise spending summary
  - Monthly spending summary
- **Categorized expenses** with emoji labels for quick scanning:
  - 🍔 Food
  - 🚗 Transport
  - 🥕 Grocery
  - 📚 Education
  - 🎮 Entertainment
  - 🎁 Gifts / Others
- **Persistent storage** via a local `expenses.csv` file
- Basic input validation (date format, non-negative amounts, valid category selection)

## Project Structure

```
.
├── main.py               # Entry point — main menu, expenses submenu, reports submenu
├── expense_manager.py    # Expense CRUD operations (create, save, update, delete)
├── reports.py            # Reporting functions (view all, category summary, monthly summary)
├── expense.py            # Expense data model
├── requirements.txt      # External dependencies (pandas, tabulate, wcwidth)
└── expenses.csv           # Generated automatically on first entry (not included)
```

### Module Overview

- **`main.py`**
  - `main()` — top-level menu (Expenses / Reports / Exit)
  - `expenses_menu()` — Add / View / Edit / Delete submenu
  - `reports_menu()` — Category Summary / Monthly Spending submenu
- **`expense_manager.py`**
  - `create_expense()` — prompt for and build a new `Expense`
  - `save_expense()` — append a new expense to `expenses.csv`
  - `update_expense()` — edit a field on an existing expense
  - `delete_expense()` — remove an existing expense (with confirmation)
- **`reports.py`**
  - `show_all_expenses()` — print every saved expense with a running total
  - `show_category_summary()` — totals spending per category
  - `show_monthly_summary()` — totals spending per month
- **`expense.py`**
  - `Expense` — data model for a single expense record

## Requirements

- Python 3.7+
- External dependencies:
  - `pandas` — used for reading/writing/editing CSV data
  - `tabulate` — used for formatted console output
  - `wcwidth` (recommended alongside `tabulate` for correct alignment with emoji/wide characters)

  Install all dependencies via `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

## Getting Started

1. Clone or download this repository.
2. Make sure `main.py`, `expense_manager.py`, `reports.py`, and `expense.py` are all in the same directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the tracker:

   ```bash
   python main.py
   ```

## Usage

On launch, you'll see the main menu:

```
====== Expense Tracker 💰 ======
1. Expenses
2. Reports
0. Exit
Select option:
```

### 1. Expenses

```
====== Expenses ======
1. Add Expense
2. View All Expenses
3. Edit Expense
4. Delete Expense
0. Back
```

- **Add Expense** — prompts for date (`DD-MM-YYYY`), name, amount, and category (chosen from a numbered list), then appends the entry to `expenses.csv`.
- **View All Expenses** — prints every saved expense in a table, including a total spent row.
- **Edit Expense** — lists all expenses with an ID, lets you pick one, pick a field to change (Date, Name, Category, or Amount), validates the new value, and saves the change back to `expenses.csv`.
- **Delete Expense** — lists all expenses with an ID, lets you pick one, shows a preview, and asks for `Y`/`N` confirmation before removing it from `expenses.csv`.

### 2. Reports

```
====== Reports ======
1. Category Summary
2. Monthly Spending
0. Back
```

- **Category Summary** — totals spending per category.
- **Monthly Spending** — totals spending per month.

### 0. Exit

Closes the application.

## Data Storage

Expenses are stored in `expenses.csv`, created automatically in the same directory the first time you add an entry. Each row contains:

| Date       | Name  | Category  | Amount |
|------------|-------|-----------|--------|
| 01-07-2026 | Lunch | 🍔 Food   | 250    |

The file uses `utf-8-sig` encoding to ensure emoji categories display correctly when opened in tools like Excel.

## Notes

- Amounts are stored as integers/floats; the `Expense` class formats them with two decimal places when printed via `repr()`.
- Invalid inputs (bad date formats, non-numeric amounts, out-of-range category/field/ID choices) are caught and the prompt repeats rather than crashing the program.
- Editing or deleting an entry re-indexes rows starting at 1 for display purposes; this ID is not stored in the CSV and may shift after a delete.

## Version History

- **v2.1** — Refactor only, no functional changes. Split the single-file CLI into `main.py`, `expense_manager.py`, and `reports.py`; renamed functions to follow PEP 8 (`snake_case`) naming conventions.
- **v2.0** — Added Edit Expense and Delete Expense functionality; restructured the CLI into Expenses and Reports submenus.