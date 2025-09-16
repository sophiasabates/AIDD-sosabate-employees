"""
    Coordinate the Model, Data, and View 
    -> Implement menu options for: 
        -> Create (validate input, save new employee)
        -> Edit (update employee attributes, but not ID)
        -> Delete (remove an employee)
        -> Display (list all employees)
        -> Quit 
    -> Hanlde errors gracefully and provide clear messages 
    -> Ensure the controller can handle both Employee and Manager objects (demonstrating polymorphism)
"""

from EmployeeData import load_employees, save_employees
from EmployeeView import display_menu, prompt_for_employee_data, display_employees, show_message
from employee import Employee, Manager

def find_employee_by_id(employees, emp_id):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    return None

def main():
    employees = load_employees()
    show_message("Welcome to the Employee Management System!")
    while True:
        display_menu()
        option = input("Select a menu option (1-5): ").strip()
        if option == "1":  # Create New Employee
            data = prompt_for_employee_data("1")
            try:
                if 'team_size' in data:
                    new_emp = Manager(data['id'], data['fname'], data['lname'], data['department'], data['phNumber'], int(data['team_size']))
                else:
                    new_emp = Employee(data['id'], data['fname'], data['lname'], data['department'], data['phNumber'])
                employees.append(new_emp)
                show_message("Employee added successfully.")
            except Exception as e:
                show_message(f"Error adding employee: {e}")
        elif option == "2":  # Edit Existing Employee
            emp_id = prompt_for_employee_data("2")
            emp = find_employee_by_id(employees, emp_id)
            if not emp:
                show_message("Employee not found.")
                continue
            show_message(f"Editing employee: {emp}")
            # Only allow editing of fields except ID
            if isinstance(emp, Manager):
                fields = ['fname', 'lname', 'department', 'phNumber', 'team_size']
            else:
                fields = ['fname', 'lname', 'department', 'phNumber']
            for field in fields:
                new_value = input(f"Enter new {field} (leave blank to keep current): ").strip()
                if new_value:
                    try:
                        if field == 'team_size' and isinstance(emp, Manager):
                            setattr(emp, field, int(new_value))
                        else:
                            setattr(emp, field, new_value)
                    except Exception as e:
                        show_message(f"Invalid value for {field}: {e}")
            show_message("Employee updated.")
        elif option == "3":  # Delete Existing Employee
            emp_id = prompt_for_employee_data("3")
            emp = find_employee_by_id(employees, emp_id)
            if emp:
                employees.remove(emp)
                show_message("Employee deleted.")
            else:
                show_message("Employee not found.")
        elif option == "4":  # Display Employees
            display_employees(employees)
        elif option == "5":  # Quit
            save_employees(employees)
            show_message("Employees saved. Goodbye!")
            break
        else:
            show_message("Invalid option. Please try again.")

if __name__ == "__main__":
    main()