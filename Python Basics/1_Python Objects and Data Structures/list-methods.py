"""
Python List Exercises
This file contains various examples to learn basic list operations in Python.
Each step is explained with comments.
"""

# Example integer list
numbers = [1, 10, 5, 16, 4, 9, 10]
# Example character list
letters = ['z', 'i', 'l', 'a', 'n']

# Finding the minimum and maximum elements in the list
print("Min numbers:", min(numbers))  # 1
print("Max numbers:", max(numbers))  # 16
print("Min letters:", min(letters))  # 'a'
print("Max letters:", max(letters))  # 'y'

# List slicing operations
print("First three elements:", numbers[:3])  # First 3 elements
print("Last three elements:", numbers[-3:])  # Last 3 elements
print("Middle elements:", numbers[2:5])  # Elements from index 2 to 4

# Adding elements to the list
print("Original list:", numbers)
numbers.append(49)  # Adds 49 to the end of the list
numbers.insert(3, 78)  # Inserts 78 at index 3
print("Updated list:", numbers)

# Removing elements from the list
# numbers.pop()  # Removes the last element
# numbers.pop(0)  # Removes the first element
# numbers.remove(10)  # Removes the first occurrence of 10

# Sorting the list
print("Before sorting:", numbers)
numbers.sort()  # Sorts in ascending order
print("Sorted list:", numbers)
numbers.reverse()  # Reverses the list
print("Reversed sorted list:", numbers)

# Finding the number of elements
print("List length:", len(numbers))
print("Count of number 10:", numbers.count(10))

# Clearing the list
numbers.clear()
print("Cleared list:", numbers)
