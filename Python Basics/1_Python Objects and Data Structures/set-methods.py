# Python String Method: endswith()
# This script demonstrates how to use the endswith() method in Python.

# Define a sample message
message = "Python"

# Check if the message ends with the letter 'n'
is_found = message.endswith('n')

# Print the result
print(f"Does the message end with 'n'? {is_found}")

# Explanation:
# - The endswith() method checks if a string ends with a specific character or substring.
# - It returns True if the string ends with the specified value; otherwise, it returns False.

# Additional Example:
message2 = "Hello, world!"
is_found2 = message2.endswith("!")
print(f"Does 'Hello, world!' end with '!'? {is_found2}")

# Output:
# Does the message end with 'n'? True
# Does 'Hello, world!' end with '!'? True