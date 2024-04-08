import json
import os
# read from json


def LoadData(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    else:
        return {}

# save to json


def SaveData(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


def AddTransaction(data):
    amount = float(input("Enter amount of money: "))
    category = input("Enter the type of expense or income: ")
    transactiontype = input("Enter type (income/expense): ").lower()
    if transactiontype not in ['income', 'expense']:
        print("Invalid transaction type.")
    if category not in data:
        data[category] = {'income': 0, 'expense': 0}
    data[category][transactiontype] += amount
    print("Added the transaction successfully!")


def ViewTransactions(data):
    print("Category\tIncome\tExense\tBalance")
    for category, values in data.items():
        income = values.get('income', 0)
        expense = values.get('expense', 0)
        balance = income - expense
        print(f'{category}\t{income}\t{expense}\t{balance}')


def main():
    filename = 'finance_data.json'
    data = LoadData(filename)
    while True:
        print('\n1. Add transaction')
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            AddTransaction(data)
        elif choice == '2':
            ViewTransactions(data)
        elif choice == '3':
            SaveData(data, file_name)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
