from expense import Expense
from datetime import datetime
import sys
import csv
import os
from tabulate import tabulate ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth

def main():
    while True:
        print("Welcome to Expense Tracker 💰")
        print("1. Add a New Entry")
        print("2. View Existing Entries")
        print("3. Exit")
        try:
            operationNum = int(input("Select any option:"))
        except ValueError:
            print("Please enter a valid number\n")
            continue
        
        try:
            if operationNum==1:
                expense = getNewEntry()
                saveNewEntry(expense)
             
            elif operationNum==2:
                displayEntries()
            elif operationNum==3:
                sys.exit()
            else:
                print("Invalid option, please try again! \n")

        except Exception as e:
            print("Something went wrong:", e)

# Add A  New Entry
def getNewEntry():
    while True:
        try:
            expense_date = datetime.strptime(input("Enter date (DD-MM-YYYY): "),"%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
    expense_name = input("Enter the expense:")
    while True:
        try:
            expense_amount = int(input("Enter Amount: "))
            if  expense_amount < 0:
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
        "🎁 Gifts / Others"]
    
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
                amount=expense_amount
                )

                return new_expense

            else:
                print("Invalid category, please try again!\n")

        except ValueError:
            print("Please enter a valid number.\n")
    
# Save the Entry
def saveNewEntry(expense:Expense):
    try:
        file_exists = os.path.exists("expenses.csv")
        with open('expenses.csv', 'a', newline="", encoding="utf-8-sig") as ExpDatabase:
            csv_writer = csv.writer(ExpDatabase)
            if not file_exists:
                csv_writer.writerow(["Date", "Name", "Category", "Amount"])

            csv_writer.writerow([expense.date.strftime("%d-%m-%Y"), expense.name, expense.category, expense.amount])
        
    
    except OSError as e:
        print(f"Error saving file: {e}")    
# View all Entries
def displayEntries():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        with open("expenses.csv", "r", newline="", encoding="utf-8-sig") as ExpDatabase:
            csv_reader = csv.reader(ExpDatabase)
            print(tabulate(csv_reader,  tablefmt="rounded_grid", colalign=("left", "left", "left", "right")))   


    except Exception as e:
        print(f"Error reading file: {e}")

    
if __name__=="__main__":
    main()


