# Lambda functions are anonymous functions that are defined using the 'lambda' keyword.
# Syntax: lambda arguments: expression
# Lambda functions are often used for short, one-line functions that don't need a name.

# Simple lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Lambda function to square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Lambda function used with map() to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # map applies lambda to each element
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Lambda function used with filter() to find even numbers in a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # filter applies lambda to each element
print(even_numbers)  # Output: [2, 4]

# Lambda function used with sorted() to sort a list of tuples by the second value
tuples = [(1, 3), (2, 2), (4, 1)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])  # lambda is used as the sorting key
print(sorted_tuples)  # Output: [(4, 1), (2, 2), (1, 3)]

# Lambda function used to return the maximum of three numbers
max_of_three = lambda a, b, c: max(a, b, c)
print(max_of_three(5, 8, 3))  # Output: 8

# Lambda function with a conditional expression (if-else)
check_even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_or_odd(7))  # Output: Odd
print(check_even_or_odd(10))  # Output: Even

# Lambda function used inside a list comprehension
cubed_numbers = [lambda x: x ** 3 for x in range(5)]
print([f(3) for f in cubed_numbers])  # Output: [27, 27, 27, 27, 27]

# Lambda function used in conjunction with reduce() to accumulate a value
from functools import reduce

numbers_to_multiply = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers_to_multiply)  # reduce applies lambda function cumulatively
print(product)  # Output: 24
