#A method is a function that is defined inside a class and is used to operate on the attributes (variables) of an object.


# Class definition
class Student:
    # Class attribute: shared by all instances of the class
    school_name = " High School"

    # Constructor (initializer method)
    def __init__(self, name, age, grade):
        self.name = name  # Instance attribute (specific to each object)
        self.age = age
        self.grade = grade

    # Method to display student information
    def introduce(self):
        print(f"Hi, I am {self.name}, a {self.age} years old student at {self.school_name}.")

    # Method to check if the student passed or failed based on grade
    def check_pass(self):
        if self.grade >= 50:
            return f"{self.name} has passed!"
        else:
            return f"{self.name} has failed."

# Creating Student objects (instances)
s1 = Student(name='Aleyna', age=16, grade=75)  # Passed student
s2 = Student(name='Eren', age=15, grade=45)  # Failed student

# Accessing methods for each student
s1.introduce()
s2.introduce()

print(s1.check_pass())  # Output: John has passed!
print(s2.check_pass())  # Output: Alice has failed.
