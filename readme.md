# Expense Tracker 💰

A simple command-line expense tracker built in Python. Log your daily expenses with a date, name, category, and amount, then view them individually, grouped by category, or summarized by month — all backed by a local CSV file.

## Features

- **Add new expense entries** — capture date, description, category, and amount
- **View all expenses** in a neatly formatted table, including a running total
- **Category summary** — see total spending grouped by category
- **Monthly spending** — see total spending grouped by month
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
├── expense_tracker.py   # Main CLI application (menu, input handling, CSV I/O, reporting)
├── expense.py             # Expense data model
└── expenses.csv            # Generated automatically on first entry (not included)
```

## Requirements

- Python 3.7+
- External dependencies:
  - [`tabulate`](https://pypi.org/project/tabulate/) — for formatted table output
  - [`pandas`](https://pypi.org/project/pandas/) — for grouping/summarizing expense data
  - [`wcwidth`](https://pypi.org/project/wcwidth/) — recommended alongside `tabulate` so emoji/wide characters align correctly in tables

Install them with:

```bash
pip install tabulate pandas wcwidth
```

## Getting Started

1. Clone or download this repository.
2. Make sure `expense.py` and `expense_tracker.py` are in the same directory.
3. Install the dependencies listed above.
4. Run the tracker:

   ```bash
   python expense_tracker.py
   ```

## Usage

On launch, you'll see a menu:

```
====== Expense Tracker 💰 ======
1. Add a New Entry
2. View All Expenses
3. Category Summary
4. Monthly Spending
5. Exit
===============================
Select any option:
```

### 1. Add a New Entry

You'll be prompted for:

- **Date** — in `DD-MM-YYYY` format
- **Expense name** — a short description (e.g., "Lunch", "Uber ride")
- **Amount** — a non-negative number (decimals allowed, e.g., `199.50`)
- **Category** — chosen from the numbered list shown on screen

The entry is then appended to `expenses.csv`.

### 2. View All Expenses

Prints every saved expense in a formatted grid table (via `tabulate`), including a final **TOTAL SPENT** row showing the sum of all amounts, prefixed with `₹`. If no `expenses.csv` file exists yet, you'll see a "No entries found." message.

### 3. Category Summary

Groups all expenses by category and prints the total spent per category in a table.

### 4. Monthly Spending

Groups all expenses by month (e.g., "July 2026") and prints the total spent per month in a table.

### 5. Exit

Closes the application.

## Data Storage

Expenses are stored in `expenses.csv`, created automatically in the same directory the first time you add an entry. Each row contains:

| Date       | Name  | Category  | Amount |
|------------|-------|-----------|--------|
| 01-07-2026 | Lunch | 🍔 Food   | 250.0  |

The file uses `utf-8-sig` encoding to ensure emoji categories display correctly when opened in tools like Excel.

## Notes

- Amounts are stored as floats, allowing decimal values (e.g., `99.99`).
- The `Expense` class formats amounts with a `$` sign and two decimal places when printed via `repr()`, while the CSV/report views use `₹` for the total — keep this in mind if you want currency symbols to match throughout.
- Invalid inputs (bad date formats, non-numeric amounts, out-of-range category choices) are caught and the prompt repeats rather than crashing the program.
- `deleteEntries()` and `editEntries()` are present as placeholder functions and not yet implemented — planned for future updates.

## Roadmap

- [ ] Implement entry editing (`editEntries`)
- [ ] Implement entry deletion (`deleteEntries`)
- [ ] Consistent currency symbol across all views
- [ ] Export/filter by date range

## License

This project currently has no license specified. Add one (e.g., MIT) if you plan to share or open-source it.