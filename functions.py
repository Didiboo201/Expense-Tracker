
import os

def add_expense(expense_data: dict):
    """Adds expenses to the corresponding file.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)

    """

def view_all_expenses(expense_data: dict):
    """Shows a complete view of all the expenses in the file.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)
    
    """

def view_expenses_by_category(expense_data: dict):
    """Shows a view of all the expenses in the file by category.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)

    """

def calculate_expenses(expense_data: dict):
    """Calculates all the expenses per month.
    
    Parameter
    ---------
    expense_data : set of data corresponding to the expenses (dict)
    
    """

def load_file(path: str):
    """Loads or creates the expenses file.
    
    Parameter
    ---------
    path : path checked to see if the expenses file already exist or not (str)
    
    """
    if not os.path.exists(path):
        #create file
        file = open('expenses.txt', 'w')
        #create empty dict
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

def save_file(expense_data: dict, file_name: str):
    """Saves all the expenses into the corresponding file.
    
    Parameters
    ----------
    expense_data : set of data corresponding to the expenses (dict)
    file_name    : name of file containing the expenses (str)
    
    """

def show_menu():
    """Shows the set of command that the user can use.
    
    """