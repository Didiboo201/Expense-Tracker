
import os

def add_expense():
    """"""

def view_all_expenses():
    """"""

def view_expenses_by_category():
    """"""

def calculate_expenses():
    """"""

def load_file(path: str):
    """Load or create the expenses file.
    
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
    
    return expense_data

def save_file():
    """"""

def show_menu():
    """"""