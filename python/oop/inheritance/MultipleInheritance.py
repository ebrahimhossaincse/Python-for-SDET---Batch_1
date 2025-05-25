class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

class Manager(Person,Employee):
    def __init__(self, name, id, position, salary):
        Person.__init__(self, name, id)
        Employee.__init__(self, position, salary)

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Position: {self.position}, Salary: {self.salary}")

manager = Manager("Ebrahim", 123, "SQA", 112022)
manager.display()