# In Python, a method is a function that is associated with an object and is called using dot notation.
# Methods are functions that belong to an object (or instance of a class).
# The primary difference between a method and a function is that methods are called on an object, while functions are not.
# A method can modify the object itself or perform operations related to that object.

# Example 1: Using list methods

my_list = [1, 2, 3]

# 'append()' is a method that adds an element to the end of the list.
my_list.append(4)  # Adding 4 to the list.
print(my_list)  # Output: [1, 2, 3, 4]

# 'pop()' is a method that removes and returns the last element from the list.
last_element = my_list.pop()  # Removing the last element (4).
print(last_element)  # Output: 4
print(my_list)  # Output: [1, 2, 3]  # The list is modified.

# Checking the type of the object
print(type(my_list))  # Output: <class 'list'>  # This confirms that my_list is a list object.

# Example 2: Using string methods

my_string = 'Hello'

# 'upper()' is a method that converts all characters of a string to uppercase.
uppercase_string = my_string.upper()
print(uppercase_string)  # Output: 'HELLO'

# The original string is not modified because strings are immutable in Python.
print(my_string)  # Output: 'Hello'

# Checking the type of the object
print(type(my_string))  # Output: <class 'str'>  # This confirms that my_string is a string object.

# Example 3: Other common methods

# List methods
my_list = [5, 10, 15, 20]
my_list.remove(10)  # Removes the first occurrence of the value 10.
print(my_list)  # Output: [5, 15, 20]

# String methods
my_string = '   Python   '
cleaned_string = my_string.strip()  # 'strip()' removes whitespace from both ends of a string.
print(cleaned_string)  # Output: 'Python'

# Example 4: Using a method on a custom class (Object-Oriented Programming)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an instance of the Person class
person = Person('Aleyna', 18)

# Calling the method 'greet()' on the person object
print(person.greet())  # Output: 'Hello, my name is Aleyna and I am 18 years old.'
