"""
    The View is responsible for ALL user input and output, no business rules 
    -> It displays menus (in a clean format), prompts, and lists to the user 
    -> It collects input data from the user (e.g. names, choices)
    -> It does NOT not know how data is stored or validated 
    -> It shows messages to the user (success, error, etc) 

    The View is like the "face" of the app, if you want to change how things look or how users interact with it, you change the View.
"""

def display_menu():
    print("\nEmployee Management System")
    print("======================================")
    print("1. Create New Employee")
    print("2. Edit Existing Employee")
    print("3. Delete Existing Employee")
    print("4. Display Employees")
    print("5. Quit")

def prompt_for_employee_data(menu_option=None):
    """
    Prompt user for menu option and, if needed, employee data fields.
    Returns the user's input as a string or dict.
    """
    if menu_option is None:
        menu_option = input("Select a menu option (1-5): ").strip()
    if menu_option == "1":
        id = input("Enter Employee ID: ").strip()
        fname = input("Enter First Name: ").strip()
        lname = input("Enter Last Name: ").strip()
        department = input("Enter Department (3 uppercase letters): ").strip()
        phNumber = input("Enter Phone Number: ").strip()
        is_manager = input("Is this employee a manager? (y/n): ").strip().lower()
        if is_manager == 'y':
            team_size = input("Enter Team Size: ").strip()
            return {'id': id, 'fname': fname, 'lname': lname, 'department': department, 'phNumber': phNumber, 'team_size': team_size}
        else:
            return {'id': id, 'fname': fname, 'lname': lname, 'department': department, 'phNumber': phNumber}
    elif menu_option == "2":
        return input("Enter the ID of the employee to edit: ").strip()
    elif menu_option == "3":
        return input("Enter the ID of the employee to delete: ").strip()
    else:
        return menu_option

def display_employees(employees):
    """
    Display a list of employees in a user-friendly format.
    """
    if not employees:
        print("No employees to display.")
        return
    print("\nEmployee List:")
    for emp in employees:
        print(emp)

def show_message(message):
    print(f"\n{message}")


