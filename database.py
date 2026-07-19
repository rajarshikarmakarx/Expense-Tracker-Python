from expense_manager import (
    create_expense,
    save_expense,
    update_expense,
    delete_expense)

from reports import (
    show_all_expenses,
    show_category_summary,
    show_monthly_spending)

from expense import Expense
from datetime import datetime
from datetime import date
import sys
import csv
import os
from tabulate import tabulate  ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth
import pandas as pd
import sqlite3


conn = sqlite3.connect('expenses.db')
cursor  = conn.cursor()

def initialize_database():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,       
            Date DATE,
            Name TEXT,
            Category TEXT,
            Amount REAL
        )
    """)
    conn.commit()


def main():
    initialize_database()
    while True:
        print("\n====== Expense Tracker 💰 ======")
        print("1. Expenses")
        print("2. Reports")
        print("0. Exit")

        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Enter a valid number\n")
            continue

        if choice == 1:
            print("\n")
            expenses_menu()

        elif choice == 2:
            print("\n")
            reports_menu()

        elif choice == 0:
            print("\n")
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid option\n")


def expenses_menu():
    while True:
        print("\n====== Expenses ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("0. Back")

        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Enter a valid number\n")
            continue

        if choice == 1:
            print("\n")
            expense = create_expense()
            save_expense(expense)

        elif choice == 2:
            print("\n")
            displayEntries()

        elif choice == 3:
            print("\n")
            update_expense()

        elif choice == 4:
            print("\n")
            delete_expense()

        elif choice == 0:
            break

        else:
            print("\n")
            print("Invalid option\n")


def reports_menu():
    while True:
        print("\n====== Reports ======")
        print("1. Category Summary")
        print("2. Monthly Spending")
        print("0. Back")

        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Enter a valid number\n")
            continue

        if choice == 1:
            print("test")
            print("\n")
            displayCategorySummary()

        # elif choice == 2:
        #     print("\n")
        #     show_monthly_spending()

        elif choice == 0:
            break

        else:
            print("\n")
            print("Invalid option\n")

def create_expense():
    while True:
        try:
            expense_date = datetime.strptime(
                input("Enter date (DD-MM-YYYY): "), "%d-%m-%Y"
            )
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
    expense_name = input("Enter the expense name:")
    while True:
        try:
            expense_amount = float(input("Enter Amount: "))
            if expense_amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
    Categories = [
        "🍔 Food",
        "🚗 Transport",
        "🥕 Grocery",
        "📚 Education",
        "🎮 Entertainment",
        "🎁 Gifts / Others",
    ]

    while True:
        for i, category in enumerate(Categories):
            print(i + 1, ".", category)

        try:
            expense_categoryIndex = int(input("Select Category: ")) - 1

            if expense_categoryIndex in range(len(Categories)):
                expense_category = Categories[expense_categoryIndex]

                new_expense = Expense(
                    date=expense_date,
                    name=expense_name,
                    category=expense_category,
                    amount=expense_amount,
                )

                return new_expense

            else:
                print("Invalid category, please try again!\n")

        except ValueError:
            print("Please enter a valid number.\n")


# Save the Entry
def save_expense(expense: Expense):
    try:
        

        cursor.execute(
            "INSERT INTO expenses (Date, Name, Category, Amount) VALUES(?, ?, ?, ?)",
            (
                expense.date.strftime("%d-%m-%Y"),
                expense.name,
                expense.category,
                expense.amount
            )
        )

        conn.commit()

    except Exception as e:
        print(f"Error saving expense: {e}")
    
def displayEntries():
    try:
        total = 0
        table = []
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        if not rows:
            print("No entries found.")
            return
        table = list(rows)
        cursor.execute("SELECT sum(amount) from expenses")
        total = cursor.fetchone()[0] or 0
        table.append(("", "", "","TOTAL SPENT", f"₹{total:.2f}"))
        headers = ["DATE", "NAME", "CATEGORY", "AMOUNT"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    except sqlite3.OperationalError:
        print("Expenses database is not initialized.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    
# Display Category-wise summary
def displayCategorySummary():
    try:
        cursor.execute("SELECT category, sum(amount) as TOTALSPENDING from expenses group by category")
        rows = cursor.fetchall()
        if not rows:
            print("No entries found.")
            return
        table = list(rows)
        headers = ["CATEGORY", "TOTAL SPENT"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
    except sqlite3.OperationalError:
        print("Expenses database is not initialized.")

    except Exception as e:
        print(f"Unexpected error: {e}")











if __name__ == "__main__":
    main()






















