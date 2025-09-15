
"""
	CREATE EMPLOYEE CLASS: ENFORCES BUSINESS RULES FOR EMPLOYEE DATA 
    # attributes: id(string), fname(string), lname(string), department(string), phNumber(string) 
    -> Use @property decorators for all attributes 
		Attributes: 
			id (str): Unique identifier for the employee (Read-only after creation)
			fname (str): First name of the employee (cannot be empty or contain digits)
			lname (str): Last name of the employee (cannot be empty or contain digits)
			department (str): Department code (Must be exactly 3 uppercase letters)
			phNumber (str): Phone number (valid 10 digits number stored unformatted).
                  -> Allow users to enter phNumber in formatted stules ((123)-456-7890 or 123.456.7890) and sanitize them into a 10-digit string for storage 
                  -> Implement a getphNumber method that returns the unformatted 10-digit phone number 
    -> ensure validation rules are applied consistently 
    -> Add inheritance and polymporphism: 
		-> Create a subclass Manager(Employee) with an additional attribute (e.g. team_size or office_number)
        -> Override a method (such as __str__ or a display() method) to demonstrate polymorphism when listing employees 

    CREATE MANAGER(EMPLOYEE) SUBCLASS:
		-> Additional attribute: team_size (int): Number of team members managed (must be a non-negative integer)
		-> Override __str__ method to include team_size in the string representation
"""

from typing import Any
import logging

class Employee:
    def __init__(self, id: str, fname: str, lname: str, department: str, phNumber: str) -> None:
        self._id = id
        self.fname = fname
        self.lname = lname
        self.department = department
        self.phNumber = phNumber

    @property
    def id(self):
        return self._id

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        if not value or any(char.isdigit() for char in value):
            raise Exception("First name cannot be empty or contain digits.")
        self._fname = value

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        if not value or any(char.isdigit() for char in value):
            raise Exception("Last name cannot be empty or contain digits.")
        self._lname = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if not (isinstance(value, str) and len(value) == 3 and value.isupper() and value.isalpha()):
            raise Exception("Department must be exactly 3 uppercase letters.")
        self._department = value

    @property
    def phNumber(self):
        return self._phNumber

    @phNumber.setter
    def phNumber(self, value):
        # Always extract digits from input, regardless of format
        digits = ''.join([c for c in value if c.isdigit()])
        if len(digits) != 10:
            raise Exception("Phone number must be a valid 10-digit number.")
        self._phNumber = digits

    def getphNumber(self):
        # Return the stored unformatted 10-digit phone number
        return self._phNumber
    
    def __str__(self):
        return f"Employee: {self.id} - {self.lname}, {self.fname} - {self.department} - {self.phNumber}"
    
# Manager subclass with inheritance and polymorphism
class Manager(Employee):
    def __init__(self, id: str, fname: str, lname: str, department: str, phNumber: str, team_size: int):
        super().__init__(id, fname, lname, department, phNumber)
        self.team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, value):
        if not isinstance(value, int) or value < 0:
            raise Exception("team_size must be a non-negative integer.")
        self._team_size = value

    def __str__(self):
        # Polymorphic string representation
        return f"Manager: {self.id} - {self.lname}, {self.fname} - {self.department} - {self.phNumber} - Team Size: {self.team_size}"


# Test code under if __name__ == "__main__" to demonstrate: 
    # Creating valid and invalid employees 
    # Creating at least one Manager object 
    # Logging errors to a file (e.g employee_test.log). 
        # The log should include a timestamp and the specific validation error triggers 
    
if __name__ == "__main__":
    # Test valid employee
    try:
        emp = Employee("1", "John", "Doe", "HRD", "(123)-456-7890")
        print("Employee created:", emp.fname, emp.lname, emp.department, emp.phNumber)
    except Exception as e:
        print("Error creating employee:", e)
        logging.error("Error creating employee: %s", e)

    # Test invalid employee (invalid first name)
    try:
        emp = Employee("2", "John3", "Doe", "HRD", "(123)-456-7890")
        print("Employee created:", emp.fname, emp.lname, emp.department, emp.phNumber)
    except Exception as e:
        print("Caught expected error (invalid first name):", e)
        logging.error("Invalid first name: %s", e)

    # Test invalid employee (invalid department)
    try:
        emp = Employee("3", "Jane", "Smith", "it", "1234567890")
    except Exception as e:
        print("Caught expected error (invalid department):", e)
        logging.error("Invalid department: %s", e)

    # Test valid manager
    try:
        mgr = Manager("4", "Alice", "Johnson", "MKT", "123.456.7890", 5)
        print("Manager created:", mgr.fname, mgr.lname, mgr.department, mgr.phNumber, mgr.team_size)
    except Exception as e:
        print("Error creating manager:", e)
        logging.error("Error creating manager: %s", e)

    # Test invalid manager (negative team size)
    try:
        mgr = Manager("5", "Bob", "Brown", "FIN", "987-654-3210", -3)
        print("Manager created:", mgr.fname, mgr.lname, mgr.department, mgr.phNumber, mgr.team_size)
    except Exception as e:
        print("Caught expected error (invalid team size):", e)
        logging.error("Invalid team size: %s", e)