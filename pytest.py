import pytest
from employee import Employee, Manager

def test_employee_creation():
    emp = Employee("1", "John", "Doe", "HRD", "1234567890")
    assert emp.id == "1"
    assert emp.fname == "John"
    assert emp.lname == "Doe"
    assert emp.department == "HRD"
    assert emp.phNumber == "1234567890"
    assert emp.getphNumber() == "1234567890"

def test_manager_creation():
    mgr = Manager("2", "Alice", "Smith", "ENG", "0987654321", 5)
    assert mgr.id == "2"
    assert mgr.fname == "Alice"
    assert mgr.lname == "Smith"
    assert mgr.department == "ENG"
    assert mgr.phNumber == "0987654321"
    assert mgr.team_size == 5
    # Polymorphism: __str__ should include 'Manager' and team size
    assert "Manager" in str(mgr)
    assert "Team Size: 5" in str(mgr)
