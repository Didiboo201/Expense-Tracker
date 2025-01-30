
expense_data = load_file("expenses.txt")

status = True

while status:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. Calculate Total Expenses")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == 1:
        add_expense(expense_data)
    elif choice == 2:
        view_all_expenses(expense_data)
    elif choice == 3:
        view_expenses_by_category(expense_data)
    elif choice == 4:
        calculate_expenses(expense_data)
    elif choice == 5:
        save_file(expense_data)
        status = False
        print("Expenses saved. Goodbye!")
    else:
        print("Invalid option. Please try again.")