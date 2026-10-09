#Employee Management System


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

class Employee:
    def __init__(self, name="", age=0, employee_id="", salary=0):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object deleted.")

class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)


def create_employee(name, age, employee_id="", salary=0):
    return Employee(name, age, employee_id, salary)

persons = []
employees = []
managers = []


while True:
    print("\n-------------------------------------------------")
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("\n-------------------------------------------------")
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Employee Details")
    print("5. Show Manager Details")
    print("6. Update Employee")
    print("7. Remove Employee")
    print("8. Check Inheritance")
    print("9. Exit")

    choice = input("\nEnter your choice:")

    if choice =="1":
        print("\n --------------------Create Person------------------")
        name = input("Enter Your Name:")
        age = int(input("Enter Your Age:"))
        person = Person(name, age)
        persons.append(person)
        print("\n Person created successfully.")
        person.display()


    elif choice == "2":
        print("\n ----------------Create Employee-----------------")
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        employee_id = input("Enter Employee ID:")
        salary = float(input("Enter Salary:"))

        employee = create_employee(
            name,
            age,
            employee_id,
            salary
        )

        employees.append(employee)
        print("\nEmployee created  successfully.")
        employee.display()


    elif choice == "3":
        
        print("\n ----------------Create Manager-----------------")
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        employee_id = input("Enter Employee ID:")
        salary = float(input("Enter Salary:"))
        department = input("Enter Department:")

        manager = Manager(
            name,
            age,
            employee_id,
            salary,
            department
        )
        managers.append(manager)
        print("\nManager created successfully.")
        manager.display()

   

    elif choice == "4":
        if len(employees) == 0:
            print("\nNo employees available.")
        else:
            print("\n -----------Employee Details------------")

            for employee in employees:
                employee.display()

    elif choice == "5":
        if len(managers) == 0:
            print("\nNo Managers available.")
        else:
            print("\n------------------Manager Details--------------------")
            for manager in managers:
                manager.display()

                
    elif choice == "6":
        if len(employees) == 0:
            print("\nNo employees available to update.")
        else:
            print("\n--------------------Update Employee----------------------")
            employee_id = input("Enter Employee ID to update:")
            found = False
            for employee in employees:
                if employee.get_employee_id() == employee_id:
                    found = True
                    print("\nEmployee found.")
                    new_name = input("Enter New Name (press Enter to keep old name):")
                    new_age = input("Enter New Age (press Enter to keep old age):")
                    new_salary = input("Enter New Salary (press Enter to keep old salary):")
                    if new_name!= "":
                        employee.name = new_name
                    if new_age!= "":
                        employee.age = int(new_age)
                    if new_salary!= "":
                        employee.set_salary(float(new_salary))

                    new_employee_id = input("Enter New Employee ID" "(press enter to keep old Id):")
                    if new_employee_id!= "":
                        employee.set_employee_id(new_employee_id)
                    print("\nEmployee updated successfully.")
                    employee.display()
                    break
            
            if not found:
                print("\nEmployee not found.")
                    

    elif choice == "7":
        if len(employees) == 0:
            print("\nNo employees available to remove.")
        else:
            print("\n ---------------------------Remove Employee--------------------------")
            employee_id = input("Enter Employee ID to remove:")
            found = False
            for employee in employees:
                  if employee.get_employee_id() == employee_id:
                      
                      found = True
                      employees.remove(employee)
                      print("\nEmployee removed successfully.")
                      break
            if found == False:
                print("\nEmployee not found.")

    elif choice == "8":
        print("\n------------------Inheritance Check-----------------")
        print("Is Manager a subclass of Employee?",
              issubclass(Manager, Employee))

    elif choice == "9":
        print("\nExiting the system.")
        print("Program ended successfully.")
        print("Goodbye!")
        break
        
    else:
        print("\nInvalid choice. Please try again.")

        
            
        























        
                   
































        


              
