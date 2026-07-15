from expense import Expense
from datetime import datetime
from datetime import date
import sys
import csv
import os
from tabulate import tabulate  ## for appropriate functioning depending on the system, install wcwidth, pip install wcwidth
import pandas as pd



def show_all_expenses():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        total = 0
        with open("expenses.csv", "r", newline="", encoding="utf-8-sig") as ExpDatabase:
            csv_reader = csv.reader(ExpDatabase)
            data = list(csv_reader)
            # calculating total spent
            for row in data[1:]:  # ignoring the header row
                total = total + float(row[3])
            data.append(["", "", "TOTAL SPENT", f"₹{total}"])

            print(
                tabulate(
                    data,
                    headers="firstrow",
                    tablefmt="grid",
                    colalign=("left", "left", "left", "right"),
                )
            )

    except Exception as e:
        print(f"Error reading file: {e}")


# Display Category-wise summary
def show_category_summary():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        df = pd.read_csv("expenses.csv")
        grouped = (df.groupby("Category", as_index=False)["Amount"].sum()).rename(
            columns={"Amount": "Total"}
        )
        result = grouped.to_dict(orient="records")
        print(tabulate(result, headers="keys", tablefmt="grid"))

    except Exception as e:
        print(f"Error reading file: {e}")


# Display Monthly Spending
def show_monthly_spending():
    if not os.path.exists("expenses.csv"):
        print("No entries found.")
        return

    try:
        df = pd.read_csv("expenses.csv")
        df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
        df["Month"] = df["Date"].dt.strftime("%B %Y")
        grouped = (df.groupby("Month", as_index=False)["Amount"].sum()).rename(
            columns={"Amount": "Total"}
        )
        result = grouped.to_dict(orient="records")
        print(tabulate(result, headers="keys", tablefmt="grid"))

    except Exception as e:
        print(f"Error reading file: {e}")
