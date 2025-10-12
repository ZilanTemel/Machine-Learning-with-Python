# In Python, scope refers to the region in which a variable is accessible.
# There are two main types of scope: local scope and global scope.

# 1. Local Scope:
# A variable is said to have a local scope if it is defined within a function.
# Local variables are only accessible within the function or block where they are defined.

def my_function():
    local_var = 10  # local_var is a local variable
    print("Inside function:", local_var)

my_function()
# print(local_var)  # This would raise an error because local_var is not accessible outside the function.

# 2. Global Scope:
# A variable is said to have a global scope if it is defined outside of all functions.
# Global variables are accessible from any part of the code, including inside functions.

global_var = 20  # global_var is a global variable

def another_function():
    print("Inside function:", global_var)  # We can access the global variable here

another_function()
print("Outside function:", global_var)  # We can also access the global variable here

# 3. Modifying a Global Variable inside a Function:
# To modify a global variable from inside a function, we use the 'global' keyword.

def modify_global():
    global global_var
    global_var = 50  # Modify the global variable

modify_global()
print("After modifying global variable:", global_var)  # Output: 50
