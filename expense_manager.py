from expense import Expense
from datetime import datetime
from datetime import date
import sys
import csv
import os
from tabulate import tabulate  ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth
import pandas as pd



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
        file_exists = os.path.exists("expenses.csv")
        with open("expenses.csv", "a", newline="", encoding="utf-8-sig") as ExpDatabase:
            csv_writer = csv.writer(ExpDatabase)
            if not file_exists:
                csv_writer.writerow(["Date", "Name", "Category", "Amount"])

            csv_writer.writerow(
                [
                    expense.date.strftime("%d-%m-%Y"),
                    expense.name,
                    expense.category,
                    expense.amount,
                ]
            )

    except OSError as e:
        print(f"Error saving file: {e}")






# Edit Entries
def update_expense():
    """
    Edit an existing expense.

    The function loads expenses.csv, displays all expenses,
    allows the user to choose one, validates the replacement
    value, updates the record, and saves the modified file.

    Returns:
        None
    """
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
    try:
        df = pd.read_csv("expenses.csv")
        # Display IDs starting from 1 instead of Pandas' default 0-based indexing
        # to make selection more intuitive for the user.
        df.index = df.index + 1
        print(tabulate(df, headers="keys"))
        print()
        # Prompt until the user selects a valid expense ID.
        while True:
            entry_input = input("Edit Expense ID to edit: ")
            print()
            if not entry_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            entryNumber = int(entry_input)

            if entryNumber < 1 or entryNumber > len(df):
                print("That entry number doesn't exist.")
                continue

            break
        # Convert the user-friendly 1-based ID into Pandas' 0-based index.    
        row_to_edit = df.iloc[entryNumber - 1].to_dict()

        # Display the current values so the user can verify
        # they selected the correct expense before editing.
        for key, value in row_to_edit.items():
            print(f"{key} - {value}")    
        print()    
            
        # ----- Select field -----  
        for i, column in enumerate(df.columns, start=1):
            print(f"{i}. {column}")
        print()
        

        # Ask which field of the selected expense should be edited.
        while True:
                field_input = input("Enter Field number to Edit:")      
                if not field_input.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue
                field_Number = int(field_input)
        
                if field_Number < 1 or field_Number > len(df.columns):
                    print("That entry number doesn't exist.")
                    continue
        
                break
        
        header = df.columns[field_Number - 1]
        value = df.iloc[entryNumber - 1, field_Number -1]
        print(f"Current {header}: {value}")
      
       # Validate the replacement value according to the field type.
        while True:
            new_input = input(f"Enter new {header}: ").strip()

            # Date must follow the DD-MM-YYYY format.
            if header == "Date":
                try:
                    datetime.strptime(new_input, "%d-%m-%Y")   # or "%Y-%m-%d"
                    break
                except ValueError:
                    print("Invalid date. Use DD-MM-YYYY.")

            # Expense names cannot be blank.
            elif header == "Name":
                if len(new_input) == 0:
                    print("Name cannot be empty.")
                else:
                     break

            # Restrict categories to the predefined list so reporting remains consistent.
            elif header == "Category":
                categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]

                if new_input.title() not in categories:
                    print(f"Choose from: {', '.join(categories)}")
                else:
                    new_input = new_input.title()
                    break

            # Amount must be a positive numeric value.
            elif header == "Amount":
                try:
                    amount = float(new_input)

                    if amount <= 0:
                        print("Amount must be greater than 0.")
                    else:
                        new_input = amount
                        break

                except ValueError:
                    print("Enter a valid number.")

        # Editing and Saving
        confirmation = input(
            "Press and Enter Y to confirm editing, N to cancel edit:"
        ).upper()
        if confirmation not in ["Y", "N"]:
            print("Please Enter a valid Input by trying again!")
        elif confirmation == "Y":
            df.iloc[entryNumber - 1, field_Number -1] = new_input
            df.to_csv("expenses.csv", index=False)
            print("Expense updated successfully!")
        elif confirmation == "N":
            print("Operation cancelled")
    # Catch unexpected file or parsing errors so the program exits gracefully.
    except Exception as e:
        print(f"Error reading file: {e}")

# Delete Entry
def delete_expense():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")

    try:
        df = pd.read_csv("expenses.csv")
        df.index = df.index + 1
        print(tabulate(df, headers="keys"))

        # Input Validation
        while True:
            entry_input = input("Enter Entry Number to Delete: ")

            if not entry_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            entryNumber = int(entry_input)

            if entryNumber < 1 or entryNumber > len(df):
                print("That entry number doesn't exist.")
                continue

            break

        print("Delete this expense? \n")
        row_to_delete = df.iloc[entryNumber - 1].to_dict()
        for key, value in row_to_delete.items():
            print(f"{key} - {value}")
        confirmation = input(
            "Press and Enter Y to confirm deletion, N to cancel deletion:"
        ).upper()
        if confirmation not in ["Y", "N"]:
            print("Please Enter a valid Input by trying again!")
        elif confirmation == "Y":
            df.drop(df.index[entryNumber - 1], inplace=True)
            df.to_csv("expenses.csv", index=False)

            print("Successfully Deleted!!")
        elif confirmation == "N":
            print("Operation cancelled")

    except Exception as e:
        print(f"Error reading file: {e}")
