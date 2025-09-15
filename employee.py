import csv
from typing import List
import logging

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
# class Employee with private attributes, getters/setters, and validation
class Employee:
	"""
	Employee class representing an employee with id, first name, last name, department, and phone number.
	Attributes are private and accessed via getters and setters with validation.
	"""

	def __init__(self, id: str, fname: str, lname: str, department: str, phNumber: str):
		self._id = id  # Set directly to make read-only
		self.fname = fname
		self.lname = lname
		self.department = department
		self.phNumber = phNumber

	# id property
	@property
	def id(self) -> str:
		"""Get the employee's ID (read-only after creation)."""
		return self._id

	# fname property
	@property
	def fname(self) -> str:
		"""Get the employee's first name."""
		return self._fname

	@fname.setter
	def fname(self, value: str):
		if not value or any(char.isdigit() for char in value):
			raise ValueError("First name cannot be empty or contain digits.")
		self._fname = value

	# lname property
	@property
	def lname(self) -> str:
		"""Get the employee's last name."""
		return self._lname

	@lname.setter
	def lname(self, value: str):
		if not value or any(char.isdigit() for char in value):
			raise ValueError("Last name cannot be empty or contain digits.")
		self._lname = value

	# department property
	@property
	def department(self) -> str:
		"""Get the employee's department (3 uppercase letters)."""
		return self._department

	@department.setter
	def department(self, value: str):
		if not (isinstance(value, str) and len(value) == 3 and value.isupper() and value.isalpha()):
			raise ValueError("Department must be exactly 3 uppercase letters.")
		self._department = value

	# phNumber property
	@property
	def phNumber(self) -> str:
		"""Get the employee's phone number formatted as (XXX)XXX-XXXX."""
		rawPhNumber = self._phNumber
		return f"({rawPhNumber[:3]}){rawPhNumber[3:6]}-{rawPhNumber[6:]}"

	@phNumber.setter
	def phNumber(self, value: str):
		if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
			raise ValueError("Phone number must be exactly 10 digits.")
		self._phNumber = value


def add_employee(employees: List["Employee"], new_employee: "Employee") -> None:
    """
    Add a new Employee to the list and save to CSV.
    Raises ValueError if an Employee with the same ID already exists.
    """
    if any(emp.id == new_employee.id for emp in employees):
        raise ValueError(f"Employee with ID {new_employee.id} already exists.")
    employees.append(new_employee)
    save_employees(employees)


def edit_employee(employees: List["Employee"], index: int, fname: str = None, lname: str = None, department: str = None, phNumber: str = None) -> None:
    """
    Edit an existing Employee's details by index. ID cannot be changed.
    Raises IndexError if index is out of range. Raises ValueError for invalid data.
    """
    if index < 0 or index >= len(employees):
        raise IndexError("Employee index out of range.")
    emp = employees[index]
    try:
        if fname is not None:
            emp.fname = fname
        if lname is not None:
            emp.lname = lname
        if department is not None:
            emp.department = department
        if phNumber is not None:
            emp.phNumber = phNumber
    except ValueError as e:
        raise ValueError(f"Invalid data: {e}")
    save_employees(employees)


def delete_employee(employees: List["Employee"], index: int) -> None:
    """
    Delete an Employee by index and save to CSV.
    Raises IndexError if index is out of range.
    """
    if index < 0 or index >= len(employees):
        raise IndexError("Employee index out of range.")
    del employees[index]
    save_employees(employees)

def display_employees(employees: list["Employee"]) -> None:
    """
    Print a numbered list of employees in the format:
    1. ID - Last, First - Department - Phone
    """
    for i, emp in enumerate(employees, start=1):
        print(f"{i}. {emp.id} - {emp.lname}, {emp.fname} - {emp.department} - {emp.phNumber}")

if __name__ == "__main__":
    logging.basicConfig(filename="employee_test.log", level=logging.INFO, format='%(message)s')
    def log(msg):
        print(msg)
        logging.info(msg)

    test_cases = [
        # Valid
        {"id": "001", "fname": "Alice", "lname": "Smith", "department": "HRD", "phNumber": "1234567890"},
        # Invalid first name (digit)
        {"id": "002", "fname": "Bob1", "lname": "Jones", "department": "ENG", "phNumber": "1234567890"},
        # Invalid last name (empty)
        {"id": "003", "fname": "Carol", "lname": "", "department": "MKT", "phNumber": "1234567890"},
        # Invalid department (not 3 uppercase)
        {"id": "004", "fname": "David", "lname": "Lee", "department": "eng", "phNumber": "1234567890"},
        # Invalid phone (not 10 digits)
        {"id": "005", "fname": "Eve", "lname": "Kim", "department": "ITD", "phNumber": "12345"},
    ]

    for case in test_cases:
        try:
            emp = Employee(**case)
            log(f"SUCCESS: Created Employee: {emp.id}, {emp.lname}, {emp.fname}, {emp.department}, {emp.phNumber}")
        except Exception as e:
            log(f"ERROR: Could not create Employee with data {case}: {e}")
