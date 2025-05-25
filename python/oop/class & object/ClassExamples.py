class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")


# Creating an object
person1 = Person("Ebrahim", 101)
person2 = Person("Samsarabbi", 103)
person1.display_info()
person2.display_info()
