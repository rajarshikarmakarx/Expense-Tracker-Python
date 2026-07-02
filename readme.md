# Expense Tracker 💰

A simple command-line expense tracker built in Python. Log your daily expenses with a date, name, category, and amount, and store them in a local CSV file for easy viewing and record-keeping.

## Features

- **Add new expense entries** — capture date, description, category, and amount
- **View existing entries** — print all saved expenses to the console
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
├── expense_tracker.py   # Main CLI application (menu, input handling, CSV I/O)
├── expense.py            # Expense data model
└── expenses.csv           # Generated automatically on first entry (not included)
```

## Requirements

- Python 3.7+
- No external dependencies — uses only the Python standard library (`csv`, `datetime`, `os`, `sys`)

## Getting Started

1. Clone or download this repository.
2. Make sure `expense.py` and `expense_tracker.py` are in the same directory.
3. Run the tracker:

   ```bash
   python expense_tracker.py
   ```

## Usage

On launch, you'll see a simple menu:

```
Welcome to Expense Tracker 💰
1. Add a New Entry
2. View Existing Entries
3. Exit
Select any option:
```

### 1. Add a New Entry

You'll be prompted for:

- **Date** — in `DD-MM-YYYY` format
- **Expense name** — a short description (e.g., "Lunch", "Uber ride")
- **Amount** — a non-negative number
- **Category** — chosen from the numbered list shown on screen

The entry is then appended to `expenses.csv`.

### 2. View Existing Entries

Prints every saved expense (date, name, category, amount) to the console. If no `expenses.csv` file exists yet, you'll see a "No entries found." message.

### 3. Exit

Closes the application.

## Data Storage

Expenses are stored in `expenses.csv`, created automatically in the same directory the first time you add an entry. Each row contains:

| Date       | Name  | Category  | Amount |
|------------|-------|-----------|--------|
| 01-07-2026 | Lunch | 🍔 Food   | 250    |

The file uses `utf-8-sig` encoding to ensure emoji categories display correctly when opened in tools like Excel.

## Notes

- Amounts are stored as integers; the `Expense` class formats them with two decimal places when printed via `repr()`.
- Invalid inputs (bad date formats, non-numeric amounts, out-of-range category choices) are caught and the prompt repeats rather than crashing the program.

## License

This project currently has no license specified. Add one (e.g., MIT) if you plan to share or open-source it.