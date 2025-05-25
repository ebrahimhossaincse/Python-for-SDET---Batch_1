class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # def display_info(self):
    #     print(f"Name: {self.name}, ID: {self.id}")

# class Student(Person):
#     def __init__(self, name, id):
#         super().__init__(name, id)

# student = Student("John", 1)
# student.display_info()


class Student(Person):
    def __init__(self, name, id, result):
        super().__init__(name, id)
        self.result = result

    def display_info(self):
        print(f"Student: {self.name}, ID: {self.id}, Result: {self.result}")


student = Student("John", "1234", 4)
student.display_info()
