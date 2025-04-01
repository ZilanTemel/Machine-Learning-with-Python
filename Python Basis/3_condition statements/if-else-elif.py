# CONDITIONAL STATEMENTS IN PYTHON (if-elif-else)

# Conditional statements allow us to execute different actions based on conditions.

# Example 1: Age Check (if-elif-else)
age = int(input("Enter your age: "))  # Get age from the user
if age < 18:
    print("Sorry, you are not an adult yet!")
elif age == 18:
    print("You are right on the border, be careful!")
else:
    print("Congratulations, you are an adult!")



# Example 2: Grading System
score = int(input("Enter your score: "))  # Get score from the user
if score >= 90:
    print("Your grade: A")
elif score >= 80:
    print("Your grade: B")
elif score >= 70:
    print("Your grade: C")
elif score >= 60:
    print("Your grade: D")
else:
    print("Your grade: F (Fail)")

