from expense import Expense
from datetime import datetime
from datetime import date
import sys
import csv
import os
from tabulate import tabulate  ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth
import pandas as pd
from expense_manager import (
    create_expense,
    save_expense,
    update_expense,
    delete_expense
)

from reports import (
    show_all_expenses,
    show_category_summary,
    show_monthly_spending
)


def main():
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
            show_all_expenses()

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
            print("\n")
            show_category_summary()

        elif choice == 2:
            print("\n")
            show_monthly_spending()

        elif choice == 0:
            break

        else:
            print("\n")
            print("Invalid option\n")


# Add A  New Entry


if __name__ == "__main__":
    main()
