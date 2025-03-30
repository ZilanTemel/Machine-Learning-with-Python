# Python Variable Naming Rules

# 1. Valid Naming Conventions
# Variable names must start with a letter or an underscore (_).
# They cannot start with a number.
valid_name = "This is valid"
_hidden_variable = 25

# Invalid example: Variable names cannot start with a number
# 1variable = "Invalid variable name"

variable1 = 100
my_variable = "hello"

# 2. Reserved Keywords Cannot Be Used
# You cannot use Python keywords like if, else, while, def, etc., as variable names.
# Example:
# def = "This is invalid"

# 3. Case Sensitivity
# Variable names are case-sensitive in Python.
name = "ZİLAN"
Name = "DERYA"

print(name)  # Outputs: ZİLAN
print(Name)  # Outputs: DERYA

# 4. Use Meaningful Names
# Use descriptive variable names that explain their purpose.
x = 25  # Not meaningful
age = 25  # Better

# 5. Use Uppercase for Constants
# Write constant values in uppercase letters.
PI = 3.14159
MAX_USERS = 100

# 6. Use Underscores for Long Names
# To improve readability, separate words with underscores.
# Bad example:
totalusersonline = 50

# Good example:
total_users_online = 50

# 7. Avoid Long Variable Names
# Keep variable names meaningful but not too long.
# Bad example:
number_of_items_in_shopping_cart = 5

# Good example:
cart_items = 5

# Python Variables: Basics and Best Practices

# 1. Declaring Variables
# Variables in Python do not require explicit declaration of their type.
# A variable's type is inferred based on the assigned value.

x = 42  # Integer
y = 3.14  # Float
z = "Hello, World!"  # String

# 2. Checking Variable Types
# You can check the type of a variable using the `type()` function.
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>

# 3. Dynamic Typing
# Variables in Python can change their type during execution.
a = 10  # Initially an integer
a = "Now a string"  # Now a string
print(a)

# 4. Multiple Assignments
# Python allows assigning values to multiple variables in a single line.
m, n, o = 1, 2, 3
print(m, n, o)

# You can also assign the same value to multiple variables.
p = q = r = 100
print(p, q, r)

# 5. Global and Local Variables
# Variables defined outside a function are global and can be accessed throughout the code.
# Variables defined inside a function are local and exist only within that function.

global_var = "I am global"

def demo_function():
    local_var = "I am local"
    print(local_var)  # Prints the local variable
    print(global_var)  # Global variables can be accessed inside functions

demo_function()
# print(local_var)  # This will raise an error because local_var is not accessible here

# 6. Memory Address of Variables
# You can check a variable's memory address using the `id()` function.
x = 42
print(id(x))  # Prints the memory address of x


# By following these rules and tips, your code will be clean, readable, and easier to debug!

