class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

while True:
    tip_angajat = input("Introduceți tipul de angajat (employee/manager/exit): ").strip().lower()

    if tip_angajat == "employee":
        name = input("Introduceți numele angajatului: ")
        salary = input("Introduceți salariul: ")
        try:
            salary = float(salary)
            emp = Employee(name, salary)
            print(emp.get_details())
        except ValueError:
            print("Salariul trebuie să fie un număr valid!")

    elif tip_angajat == "manager":
        name = input("Introduceți numele managerului: ")
        salary = input("Introduceți salariul: ")
        department = input("Introduceți departamentul: ")
        try:
            salary = float(salary)
            mgr = Manager(name, salary, department)
            print(mgr.get_details())
        except ValueError:
            print("Salariul trebuie să fie un număr valid!")

    elif tip_angajat == "exit":
        break

    else:
        print("Tip invalid! Alegeți între 'employee', 'manager' sau 'exit'.")
