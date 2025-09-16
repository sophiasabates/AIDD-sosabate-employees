Step 1: Create the Empployee Class (Business Logic)
Copilot Response: The Employee class has been created in employee.py with private attributes, getters/setters, and all specified validation rules. Each method and property includes docstrings for clarity. Let me know if you want to see usage examples or add tests.
Copilot Results: Copilot generated the full employee class. The only thing that Copilot didn't include was the "str", or type hints to the parameters, so I added those. 

Step 2: Add Read-Only and Formatting Rules 
Copilot Response: Here’s what was changed in the Employee class - The employee ID is now read-only after creation. You can set it only during initialization; there is no setter for id anymore.The phone number is now formatted as (XXX)XXX-XXXX when accessed via the phNumber property, instead of returning the raw digits.
Copilot Results: Copulot got the read-only attributes for Employee ID correct. Also, the phone number is in the correct format. I asked for further clarification on this to make sure it was correct, and the variable raw is used to store the unformatted phone number string, making it easier to display formatted but keeping the original value unchanged (stored as digits). However, I did chanange the variable name from raw to rawPhNumber because it made more sense to me. 

Step 3: Build CSV Load and Save Functions 
Copilot Response: Python functions to load and save a list of Employee objects from a CSV file named employee_data.csv have been added. The CSV columns are id, fname, lname, department, and phNumber. The loader reads these columns and creates Employee objects; the saver writes the attributes (with the raw phone number) back to the CSV. Let me know if you want usage examples or tests!
Copilot Results: Copilot gave employees = [], which creates an empty list. However, I think it should be List[Employee] = [] instead, because it makes it clear that the list should only contain Employee objects using type hints. Also it didn't create a variable with CSV_FIle = csv file where employee data is stored but rather called it in both the load and save functions, so I added this manually for simplicity and clarification. 
Step 4: Add Create, Edit, Delete Functions 
Copilot Response: add_employee-> adds a new Employee to the list and saves to CSV. Raises an error if the ID already exists. Edit_employee -> edits an exisiting Employee (except ID) by index, with validation and error handling. delete_employee -> deletes and Employee by index and saves to CSV and raises and error if the index is invalid. 
Copilot Results: Copilot created a add_emplopyee instead of create_emplopyee function, so I had to manually change that. 

Step 5: Build Display Function 
Copilot Response: Added a function print_employees that prints a numbered list of employees in the format -> 1.ID - Last, First - Department - Phone. You can now call print_employees(employees) to display employee list as requested
Copilot Results: I had to change the name of the function from print_employees to display_functions according to the expected outcome.  Howevever, it was an a neatly formatted output. 

Step 6: Build a CLI Menu (User Interface)
Copilot Response: THe main loop was added to the main employee.py file but was not added to an EmployeeApp.py file with a menu-driven CLI program. 
Copilot Results: The Copilot didn't put validation in the UI code, but rather the validation logic already present in the Employee class. However, I did create a seperate EmployeeApp.py to put the menu-driven CLI program wiht the business logic still living in employee.py. 

Step 7: Test Valid and Invalid Data 
Copilot Response: Test code has been added to the bottom of employee.py that will try to create Employee objects with both valid and invalid data and log successes adn errors to employee_test.log
Copilot Results: It put import logging in the main function instead of having it at the top with the rest of the imports so I edited that. I tested the valid/invalid employee test by running the test and it provided the correct data. 


________________________________________________________________________________________
Assignment_3 Prompts: 

Copilot Prompt: Part 1 
Write a python class called Employee with the following attributes and ensure to follow the validation rules are applied consistently. For all of the attributes use @property decorators (no old-style getters and setters) 

id (str): Unique identifier for the employee 
fname (str): First name of the employee 
lname (str): Last name of the employee
department (str): Department code 
phNumber (str): Phone number 
Here are the following validation rules, that must be applied consistently: 

id (str): Read-only after creation
fname (str): cannot be empty or contain digits
lname (str): cannot be empty or contain digits
department (str): Must be exactly 3 uppercase letters
phNumber (str): must be a valid 10-digit number stored unformatted
    Allow users to enter phone numbers in formatted styles such as (123)456-7890 or 123.456.7890 
    Implement a getphNumber method that returns the user inputed phone numbers and then sanitize them into a 10-digit string for storage that returns that returns the unformatted 10-digit phone number. 
Copilot Edits/Results: 
Wanted me to use the re module (used for regular expressions to remove all non-digit characters froma string) for getphNumber. However, I would rather sanitize them into a 10-digit string for storage without important re module.
Follow-up Prompt: 
Is there another way to allow users to enter a number in formatted styles (e.g (123)-456-7890 or 123.456.7890) and sanitize them into a 10-digit storage. With implementing a getphNumber method that returns the unformatted 10-digit phone number?
Follow-up Copilot Edits/Results: 
It corrected the getphNumber to allow a user to enter formatted and then store it unformatted. However, I didnt like how it used raise valueError so I changed it to raise Exception ensuring that validations rules are applied consistently. After this, the code worked (checked against python test at the bottom of employee.py file) and made sense to me. 



Copilot Prompt: 
Please add inheritance and polymorphism to this next part. Write a python subclass Manager(Employee) with one additional attribute: team_size. For this attribute ensure proper validation rules are applied consistently, such as team_size cannot be negative and use @property decorators for this new attribute: team_size. 
Override a method (such as str or a display() method to demonstrate polymorphism when listing or printing employees. 
Copilot Edits/Results: 
Copilot added a Manager subclass inheriting from Employee, with a team_size attribute that uses property decorators and enforces non0negative integer validation (EX: cannot be negative amount of employees on a team that manager manages). The __str__ method is overridden to demonstrate polymorphism when listing employees. I checked this to make sure it works by adding valid manager/ivalid manager testing at the bottom of employee.py file. 
Follow-up Copilot Prompt: 
I feel like I should have a __str__ method in employee class when listing employees since im overriding the method in subclass Manager(Employee), there should be something to override? what is best practice?
Follow-up Copilot Edits/Results: 
By following-up with this prompt I was able to get confirmatin that it is best practice to define a __str__ method in Employee class if I am overriding it in the Manager subclass. This way all Employee objecs have a meanfinful string representation, and the polymorphic behavior is clear and intentional. Therefore, I updated the employee class to include this __str__ method. 


Copilot Prompt: Part 2
Write python functions to load and save a list of employee objects from a CSV file named employee_data.csv. 
Load_employees: Load employees from a CSV file into a list of Employee or Manager objects 
Return a list of employee and manager objects 
Save_employees: Save the list of Employee objects to the csv file. 
Return a function writing back to CSV 

The CSV columns should be id, fname, lname, department, phNumber and team_size for subclass Manager(Employee). For regular employees, not managers, team_size should be 

Remember to call Employee when creating objects. If the file does not exist, return an empty list. 


Copilot Edits/Results: 
Overall Copilot provided a good solution to this prompt. However, I didn't like how it used import os and os.path.exists because we haven't really honed in on that too much in class. 
Follow-up Copilot Prompt: 
Please don't use import os. Instead use import from typing import list. 
Follow-up Edits/Results: 
I did have to fix the imports based on the first prompt. 


Copilot Prompt: Part 3 
Write the following Python functions in EmployeeView.py
display_menu() 
This function displays the menu 

Example display_menu():
Employee Management System
1. Create New Employee
2. Edit Existing Employee
3. Delete Existing Employee
4. Display Employees
5. Quit


prompt_for_employee_data() 
This function should prompt the user to select a menu option and then based on that prompt the user for employee data fields. 
Return user’s input as a string 
display_employees() 
This function should display employees in a clean user-friendly format. 
This function is called by the Controller whenever the user needs to see the list 
show_message()
This function should show messages to the user 

Copilot Edits/Results: 
The EmployeeView.py should only handle input and output; it should not handle business rules. 
Copilot created the functions only handling input and output, keeping business logic seperate. 



Copilot Prompt: Part 4
In EmployeeApp.py, please help me with the controller in the MVC architecture. Implement menu options that coordinate the flow of the application: 
It does NOT contain business rules (those are in the model) 
It does NOT handle user input/output (those are in the view) 
It does NOT handle file/database access (that's in the data layer) 

The controller's job is to: 
Receive user actions from the view 
Manipulate model objects (employee) 
Save/load data using the data layer 
Tell the view what to display 

For this, I would like you to write a Python main loop that: 
Loads employees from CSV at startup 
Shows a menu with options for Add, Edit, Delete, List, and Quit 
Calls the correct function based on input 
Handles invalid input gracefully 

This will result in an implementation  menu with options for: 
Create (validate input, save new employee) 
Edit (update employee attributes, but not ID) 
Delete (remove and employee) 
Display (list all employees) 
Quit 

Please ensure that the controller and user interface can handle both Employee and Manager objects (demonstrating polymorphism). 
Copilot Edit/Results: 
Copilot produced the controller in the MVC architecture, loading employees, showing a menu with the otions, calling the correct function based on user input, handles both employee and manager objects (polymorphism), and does not contain business rules, input/ouput, or file access logic (those are handled in the model, view, and data layers). This keeps the code modular and maintainable. 
Copilot Follow-up Propmpt: 
The code is now throwing errors, unable to run accurately. So I had it fix the errors in the main loop, that weren't allowing the funcction to be complete and correct. 
Copilot Follow-up Response: 
I ran the pyhton test, by inserting an employee with their necessary attributes, and then selected display employees. This code worked correctly, and after displaying employees I saw the employee I had created. After, I ran quit I was able to see the employee_data.csv was created. 


Copilot Edits/Results: 

Copilot Prompt: Extra Credit 
Help me create an Automated Testing pytest.py file with 1-2 unit tests for my employee/manager classes. This will demonstrate knoweldge of automated testing practices. 
Copilot Edits/Results: 
These creates tests, check for both the employee and manager class, that check object creation, attribute values, and demonstrate polymorphism via the managers string representation. 



OVERALL: 
AI didn't generate substrings for most functions or aspects of the python files, so I had to go in and manually add those. However, I do feel like this allowed me to better understand the processes and functionality of the system. 