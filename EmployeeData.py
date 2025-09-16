
"""
    Implement functions to:
        -> load_employees: Load employees from a CSV file into a list of Employee or Manager objects
        -> save_employees: Save the list of Employee objects to the CSV file
"""


import csv
from typing import List
from employee import Employee, Manager

CSV_FILE = "employee_data.csv"

def load_employees() -> List[Employee]:
    """
    Load employees from CSV file. Returns a list of Employee and Manager objects.
    If file does not exist, returns an empty list.
    """
    employee_list: List[Employee] = []
    try:
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header if present
            for row in reader:
                # Accept both Employee and Manager rows
                if len(row) == 6 and row[5].strip() != "":
                    id, fname, lname, department, phNumber, team_size = row
                    try:
                        employee = Manager(id, fname, lname, department, phNumber, int(team_size))
                        employee_list.append(employee)
                    except Exception:
                        continue
                elif len(row) >= 5:
                    id, fname, lname, department, phNumber = row[:5]
                    try:
                        employee = Employee(id, fname, lname, department, phNumber)
                        employee_list.append(employee)
                    except Exception:
                        continue
    except FileNotFoundError:
        pass  # No file yet = no employees
    return employee_list

def save_employees(employees: List[Employee]):
    """
    Save a list of Employee/Manager objects to the CSV file.
    """
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'fname', 'lname', 'department', 'phNumber', 'team_size']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for emp in employees:
            row = {
                'id': emp.id,
                'fname': emp.fname,
                'lname': emp.lname,
                'department': emp.department,
                'phNumber': emp.phNumber,
                'team_size': emp.team_size if isinstance(emp, Manager) else ''
            }
            writer.writerow(row)
