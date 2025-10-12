# In Python, functions are created using the 'def' keyword.
# The syntax is: def function_name(parameters): followed by the indented code block.
# Functions allow you to write reusable blocks of code that can be called whenever needed.

# Function without parameters (No arguments)
def greet():
    print("Hello, World!")  # This function doesn't take any arguments.
greet()  # Calling the function

# Function with a parameter (one argument)
def greet_person(name):
    print(f"Hello, {name}!")  # This function uses the 'name' parameter.
greet_person("Alice")  # Passing "Alice" as the argument.

# Function with return value
def add(a, b):
    return a + b  # Returns the sum of 'a' and 'b'.
result = add(3, 5)  # Calling the function and storing the result.
print(result)  # Output will be: 8

# Function with default parameters
def greet(name="Guest", age=18):
    print(f"Hello, {name}! You are {age} years old.")
greet()  # Uses default values for name and age.
greet("John", 25)  # Provides custom values for name and age.

# Function with *args (arbitrary number of positional arguments)
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num  # Adds up all the numbers passed to the function.
    return total
print(sum_numbers(1, 2, 3))  # Adds 1 + 2 + 3, returns 6.
print(sum_numbers(10, 20))  # Adds 10 + 20, returns 30.

# Function with **kwargs (arbitrary number of keyword arguments)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Prints each key-value pair from kwargs.
display_info(name="Alice", age=25, city="New York")

# Function using both *args and **kwargs
def mixed_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")  # 'a' and 'b' are normal parameters.
    print(f"Additional positional arguments: {args}")  # *args contains extra positional arguments.
    print(f"Additional keyword arguments: {kwargs}")  # **kwargs contains extra keyword arguments.

# Calling the mixed function with both positional and keyword arguments
mixed_function(1, 2, 3, 4, 5, city="London", country="UK")

# Function with a return value and printing multiple outputs
def multiply(a, b):
    return a * b  # Returns the product of 'a' and 'b'.
product = multiply(4, 5)
print(f"The product of 4 and 5 is: {product}")

# Function with a list passed as an argument (modifying a mutable object)
def add_item_to_list(item, my_list):
    my_list.append(item)  # Modifies the list by adding an item.
    print(my_list)  # Prints the updated list.

my_list = [1, 2, 3]
add_item_to_list(4, my_list)  # Adds 4 to the list and prints the updated list.
