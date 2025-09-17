def test_employee_creation():
def test_manager_creation():
# Automated tests for Employee and Manager classes
import pytest
from employee import Employee, Manager

# Test creation and attribute validation for Employee
def test_employee_creation():
    # Create an Employee object with valid data
    emp = Employee("1", "John", "Doe", "HRD", "1234567890")
    # Check that all attributes are set correctly
    assert emp.id == "1"  # ID should match
    assert emp.fname == "John"  # First name should match
    assert emp.lname == "Doe"  # Last name should match
    assert emp.department == "HRD"  # Department should match
    assert emp.phNumber == "1234567890"  # Phone number should be stored as digits
    assert emp.getphNumber() == "1234567890"  # getphNumber returns unformatted phone number

# Test creation and attribute validation for Manager (subclass of Employee)
def test_manager_creation():
    # Create a Manager object with valid data and a team size
    mgr = Manager("2", "Alice", "Smith", "ENG", "0987654321", 5)
    # Check that all inherited and new attributes are set correctly
    assert mgr.id == "2"  # ID should match
    assert mgr.fname == "Alice"  # First name should match
    assert mgr.lname == "Smith"  # Last name should match
    assert mgr.department == "ENG"  # Department should match
    assert mgr.phNumber == "0987654321"  # Phone number should be stored as digits
    assert mgr.team_size == 5  # Team size should match
    # Polymorphism: __str__ should include 'Manager' and team size
    assert "Manager" in str(mgr)  # __str__ output should indicate Manager
    assert "Team Size: 5" in str(mgr)  # __str__ output should show team size
