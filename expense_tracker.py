from expense import Expense
from datetime import datetime
import sys
import csv
import os
def main():
    while True:
        print("Welcome to Expense Tracker 💰")
        print("1. Add a New Entry")
        print("2. View Existing Entries")
        print("3. Exit")
        operationNum = int(input("Select any option:"))
        if operationNum==1:
            expense = getNewEntry()
            saveNewEntry(expense)
             
        elif operationNum==2:
            displayEntries()
        elif operationNum==3:
            sys.exit()
        else:
            print("Invalid option, please try again! \n")

# Add A  New Entry
def getNewEntry():
    expense_date = datetime.strptime(input("Enter date (DD-MM-YYYY): "), "%d-%m-%Y")
    expense_name = input("Enter the expense:")
    expense_amount = int(input("Enter Amount:"))
    Categories = [
        "🍔 Food",
        "🚗 Transport",
        "🥕 Grocery",
        "📚 Education",
        "🎮 Entertainment",
        "🎁 Gifts / Others"]
    
    while True:
        for i, category in enumerate(Categories):
            print(i+1, f"." ,category)
        expense_categoryIndex = int(input("Select Category:")) -1
        if expense_categoryIndex in range(len(Categories)):
            expense_category = Categories[expense_categoryIndex]
            new_expense = Expense(date = expense_date, name = expense_name, category= expense_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category, please try again! \n")
    
# Save the Entry
def saveNewEntry(expense:Expense):
    file_exists = os.path.exists("expenses.csv")
    with open('expenses.csv', 'a', newline="", encoding="utf-8-sig") as ExpDatabase:
        csv_writer = csv.writer(ExpDatabase)
        if not file_exists:
            csv_writer.writerow(["Date", "Name", "Category", "Amount"])

        csv_writer.writerow([expense.date.strftime("%d-%m-%Y"), expense.name, expense.category, expense.amount])
        
        
# View all Entries
def displayEntries():
    with open('expenses.csv', 'r', newline="", encoding="utf-8-sig") as ExpDatabase:
        file_exists = os.path.exists("expenses.csv")
        csv_reader = csv.reader(ExpDatabase)
        if not file_exists:
            print("Invalid funtion, entries dont exist")
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])

    
if __name__=="__main__":
    main()


