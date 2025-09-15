"""
    Implement functions to: 
        -> load_employees: Load employees from a CSV file into a list of Employee or Manager objects 
        -> save_employees: Save the list of Employee objects to the CSV file
"""

# File to store employee data
CSV_FILE = "employee_data.csv"

def load_employees() -> List["Employee"]:
    """
    Load a list of Employee objects from a CSV file.
    The CSV must have columns: id, fname, lname, department, phNumber.
    Returns a list of Employee objects.
    """
    employees: List["Employee"] = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emp = Employee(
                id=row['id'],
                fname=row['fname'],
                lname=row['lname'],
                department=row['department'],
                phNumber=row['phNumber']
            )
            employees.append(emp)
    return employees


def save_employees(employees: List["Employee"]) -> None:
    """
    Save a list of Employee objects to a CSV file.
    The CSV will have columns: id, fname, lname, department, phNumber.
    """
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'fname', 'lname', 'department', 'phNumber']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for emp in employees:
            writer.writerow({
                'id': emp.id,
                'fname': emp.fname,
                'lname': emp.lname,
                'department': emp.department,
                'phNumber': emp.phNumber.replace('(','').replace(')','').replace('-','')
            })

