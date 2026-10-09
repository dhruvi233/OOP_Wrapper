🧠 Employee Management System
📌 Project Overview
The Employee Management System is a Python-based, menu-driven console application developed using Object-Oriented Programming (OOP) concepts.
This project allows users to create and manage Person, Employee, and Manager objects. Users can create records, display employee and manager details, update employee information, remove employee records, and check inheritance.
The project demonstrates classes, objects, constructors, destructors, encapsulation, getters and setters, inheritance, method overriding, super(), and issubclass().

🎥 Project Video Demonstration
https://drive.google.com/file/d/1QidYFFa2_Z1UirJ4Y7cCQ84ZWx5SSELQ/view?usp=sharing


🎯 Objectives
●	Understand the fundamentals of Object-Oriented Programming in Python.
●	Create and manage Person, Employee, and Manager objects.
●	Implement encapsulation using private attributes.
●	Use constructors and destructors.
●	Demonstrate inheritance and method overriding.
●	Use getters and setters to access and modify private attributes.
●	Implement employee creation, display, update, and removal operations.
●	Create a menu-driven console application using loops and conditional statements.


🛠️ Features
👤 Person Management
●	Create a Person object.
●	Store the person's name and age.
●	Display person details.
👨‍💼 Employee Management
●	Create an Employee object.
●	Store employee name, age, employee ID, and salary.
●	Display employee details.
●	Update employee name, age, employee ID, and salary.
●	Remove an employee using their employee ID.


🏢 Manager Management
●	Create a Manager object.
●	Store the manager's name, age, employee ID, salary, and department.
●	Display manager details.
●	Inherit common employee attributes and methods from Employee.


🔍 Inheritance Check
●	Use issubclass() to check whether Manager is a subclass of Employee.
📋 Menu-Driven Interface


●	Display a menu of available operations.
●	Allow users to select an operation.
●	Continue running until the user chooses Exit.
●	Display an error message for invalid menu choices.


🧠 Python Concepts Used
1. Classes and Objects
Person, Employee, and Manager are classes. Objects store and display information.
2. Constructor (__init__())
Initializes attributes when an object is created. Employee uses default arguments for optional values.
3. Encapsulation
Employee ID and salary use private attributes: self.__employee_id and self.__salary.
4. Getters and Setters
get_employee_id() retrieves the ID; set_employee_id() updates it; get_salary() retrieves salary; set_salary() updates it.
5. Inheritance
Manager inherits common attributes and methods from Employee.
6. Method Overriding
Manager defines its own display() method, overriding Employee.display().
7. super()
Calls the parent class constructor from Manager to initialize common employee attributes.
8. Destructor (__del__())
Defines a method that prints a message when an Employee object is finalized.
9. issubclass()
Checks whether Manager inherits from Employee.
10. Functions
create_employee() creates and returns an Employee object.
11. Lists
persons stores Person objects; employees stores Employee objects; managers stores Manager objects.
12. Loops and Conditional Statements
A while loop repeats the menu; if/elif/else handle choices; for loops search and display records.


📋 Program Menu
-------------------------------------------------
EMPLOYEE MANAGEMENT SYSTEM
-------------------------------------------------
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Employee Details
5. Show Manager Details
6. Update Employee
7. Remove Employee
8. Check Inheritance
9. Exit
💻 Sample Program Output
Creating an Employee
----------------Create Employee-----------------
Enter Name: Riya
Enter Age: 22
Enter Employee ID: E101
Enter Salary: 25000

Employee created successfully.
Employee Details:
Name: Riya
Age: 22
Employee ID: E101
Salary: 25000.0
Creating a Manager
----------------Create Manager-----------------
Enter Name: Rahul
Enter Age: 30
Enter Employee ID: M101
Enter Salary: 45000
Enter Department: Finance

Manager created successfully.
Manager Details:
Name: Rahul
Age: 30
Employee ID: M101
Salary: 45000.0
Department: Finance
Checking Inheritance
------------------Inheritance Check-----------------
Is Manager a subclass of Employee? True
Removing an Employee
Enter Employee ID to remove: E101
Employee removed successfully.
Exiting the Program
Exiting the system.
Program ended successfully.
Goodbye!
📝 Input Validation Rules
●	Age must be entered as an integer.
●	Salary must be entered as a numeric value.
●	Employee ID identifies records for updating and removal.
●	Pressing Enter during an employee update keeps the existing value.
●	Invalid menu choices display an error message.
●	An employee must exist in the Employee list before it can be updated or removed.
Note: The current program does not include exception handling for invalid age or salary input.
▶️ How to Run the Program
1.	Install Python on your computer.
2.	Open IDLE, VS Code, or another Python editor.
3.	Save the source code as employee_management_system.py.
4.	Run the Python file.
5.	Select an option from the displayed menu.
6.	Enter the required information.
7.	Choose Exit when you finish.
📂 Program Structure
Employee_Management_System/
│
├── employee_management_system.py
└── README.md
📝 Assumptions
●	Employee records are stored in lists while the program is running.
●	Records are not saved permanently to a file or database.
●	Employee IDs are used to search for employee records.
●	Update and removal operations apply to the Employee list, not the separate Manager list.
●	Person and Manager objects are stored in their respective lists.
●	The program runs until the user selects Exit.

👩‍💻 Author
Dhruvi Manoj Das
Python Project – Employee Management System
📄 License
This project is created for educational and learning purposes.
✨ Happy Coding! ✨
