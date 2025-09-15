from employee import load_employees, save_employees, add_employee, edit_employee, delete_employee, print_employees, Employee

def main():
    employees = load_employees()
    while True:
        print("\nEmployee Manager Menu:")
        print("1. List Employees")
        print("2. Add Employee")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Quit")
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            print_employees(employees)
        elif choice == '2':
            try:
                id = input("Enter ID: ").strip()
                fname = input("Enter First Name: ").strip()
                lname = input("Enter Last Name: ").strip()
                department = input("Enter Department (3 uppercase letters): ").strip()
                phNumber = input("Enter Phone Number (10 digits): ").strip()
                new_emp = Employee(id=id, fname=fname, lname=lname, department=department, phNumber=phNumber)
                add_employee(employees, new_emp)
                print("Employee added.")
            except Exception as e:
                print(f"Error adding employee: {e}")
        elif choice == '3':
            try:
                idx = int(input("Enter employee number to edit: ")) - 1
                fname = input("Enter new First Name (leave blank to keep current): ").strip() or None
                lname = input("Enter new Last Name (leave blank to keep current): ").strip() or None
                department = input("Enter new Department (leave blank to keep current): ").strip() or None
                phNumber = input("Enter new Phone Number (leave blank to keep current): ").strip() or None
                edit_employee(employees, idx, fname, lname, department, phNumber)
                print("Employee updated.")
            except Exception as e:
                print(f"Error editing employee: {e}")
        elif choice == '4':
            try:
                idx = int(input("Enter employee number to delete: ")) - 1
                delete_employee(employees, idx)
                print("Employee deleted.")
            except Exception as e:
                print(f"Error deleting employee: {e}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
