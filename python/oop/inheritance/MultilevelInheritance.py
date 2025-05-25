class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        Employee.__init__(self, name, employee_id)
        self.department = department

class Director(Manager):
    def __init__(self, name, employee_id, department, region):
        super().__init__(name,employee_id,department)
        self.region = region

    def display(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Region: {self.region}")


director = Director("Sajid", 12, "IT", "Dhaka")
director.display()