
import os

def add_expense(expense_data: dict):
    """Adds expenses to the corresponding file.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)

    """
    category = input("Enter the category here! ")
    amount = float(input("Enter the amount here! "))
    description = input("Enter the description here! ")
    date = input("Enter the date (YYYY-MM-DD) here! ")

    if category not in expense_data:
        expense_data[category] = []

    expense_data[category].append([date, amount, description])
    print("Expense added!")

def view_all_expenses(expense_data: dict):
    """Shows a complete view of all the expenses in the file.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)
    
    """
    if expense_data == {}:
        return "There is no expenses yet!"
    
    for category, items in expense_data.items():
        print(f"\nCategory : {category}")
        for item in items:
            print(f"Date: {item[0]}, Amount: ${item[1]:.2f}, Description: {item[2]}") 

def view_expenses_by_category(expense_data: dict):
    """Shows a view of all the expenses in the file by category.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)

    """
    category = input("Enter the category: ")

    if category in expense_data:
        print(f"\nCategory : {category}")
        for item in expense_data[category]:
            print(f"Date: {item[0]}, Amount: ${item[1]:.2f}, Description: {item[2]}")
    else:
        print("This category doesn't exist yet!")


def calculate_expenses(expense_data: dict):
    """Calculates all the expenses.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)
    
    """
    total = 0
    for items in expense_data.values():
        total += sum(item[1] for item in items)
    print(f"Total expenses: ${total}:.2f")

def load_file(path: str):
    """Loads or creates the expenses file.
    
    Parameter
    ---------
    path : path checked to see if the expenses file already exist or not (str)
    
    """
    if not os.path.exists(path):
        file = open('expenses.txt', 'w')

        expense_data = {}

        file.close()
        return expense_data
    
    #load data
    expense_data = {}

    file = open('expenses.txt', 'r')
    for line in file:
        #Divide lines into different colones : Category | date, amount, description
        colones = line.split('|')
        #First colone = category
        category = colones[0]
        #Separate each element by a comma (except for category)
        expense_data[category] = [item.split(',') for item in colones[1:]]
        #Convert amount into float
        for item in expense_data[category]:
            item[1] = float(item[1])
    file.close()
    return expense_data

def save_file(expense_data: dict):
    """Saves all the expenses into the corresponding file.
    
    Parameters
    ----------
    expense_data : set of data corresponding to the expenses (dict)
    
    """
    file = open('expenses.txt', 'w')
    for category, items in expense_data.items():
        line = category + "|" + "|".join(",".join(map(str, item)) for item in items)
        file.write(line + "\n")
    file.close()


def show_menu():
    """Shows the set of command that the user can use.
    
    """