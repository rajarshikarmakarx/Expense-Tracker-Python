from expense import Expense
from datetime import datetime
from datetime import date
import sys
import csv
import os
from tabulate import tabulate ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth
import pandas as pd

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
            expenses_menu()

        elif choice == 2:
            reports_menu()

        elif choice == 0:
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
            expense = getNewEntry()
            saveNewEntry(expense)

        elif choice == 2:
            displayEntries()

        elif choice == 3:
            editEntries()

        elif choice == 4:
            deleteEntries()

        elif choice == 0:
            break

        else:
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
            displayCategorySummary()

        elif choice == 2:
            displayMonthlySpending()

        elif choice == 0:
            break

        else:
            print("Invalid option\n")

    







# Add A  New Entry
def getNewEntry():
    while True:
        try:
            expense_date = datetime.strptime(input("Enter date (DD-MM-YYYY): "),"%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
    expense_name = input("Enter the expense name:")
    while True:
        try:
            expense_amount = float(input("Enter Amount: "))
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
        total = 0
        with open("expenses.csv", "r", newline="", encoding="utf-8-sig") as ExpDatabase:
            csv_reader = csv.reader(ExpDatabase)
            data = list(csv_reader)
            #calculating total spent
            for row in data[1:]: #ignoring the header row
                total = total+float(row[3])
            data.append([
                "", "", "TOTAL SPENT", f"₹{total}"
            ])



            print(tabulate(data,  headers="firstrow",tablefmt="grid", colalign=("left", "left", "left", "right")))   
            
           
    
        
    except Exception as e:
        print(f"Error reading file: {e}")


#Display Category-wise summary
def displayCategorySummary():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        df = pd.read_csv("expenses.csv")
        grouped = (df.groupby("Category", as_index=False)["Amount"].sum()).rename(columns = {"Amount": "Total"})
        result = grouped.to_dict(orient = "records")
        print(tabulate(result, headers = "keys", tablefmt="grid"))
        
    except Exception as e:
        print(f"Error reading file: {e}")

def displayMonthlySpending():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        df = pd.read_csv("expenses.csv")
        df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
        df["Month"] = df["Date"].dt.strftime("%B %Y")
        grouped = (df.groupby("Month", as_index=False)["Amount"].sum()).rename(columns = {"Amount": "Total"})
        result = grouped.to_dict(orient = "records")
        print(tabulate(result, headers = "keys", tablefmt="grid"))
        
    except Exception as e:
        print(f"Error reading file: {e}")

def deleteEntries():
    pass

def editEntries():
    pass


    
if __name__=="__main__":
    main()


