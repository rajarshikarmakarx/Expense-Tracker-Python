from expense import Expense
from datetime import datetime
import sys

def main():
    while True:
        print("Welcome to Expense Tracker 💰")
        print("1. Add a New Entry")
        print("2. View Existing Entries")
        print("3. Exit")
        operationNum = int(input("Select any option:"))
        if operationNum==1:
             expense = getNewEntry()
             print(expense)
             
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
def saveNewEntry():
    pass
# View all Entries
def displayEntries():
    print("Hiiiiiii testingggg ")



if __name__=="__main__":
    main()


