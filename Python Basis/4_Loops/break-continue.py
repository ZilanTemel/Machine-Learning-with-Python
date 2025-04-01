# Break Example
# The 'break' statement is used to exit the loop completely when a condition is met.
for x in range(10):
    if x == 5:  # If x is equal to 5, exit the loop
        print("Breaking at x =", x)
        break  # Exits the loop
    print(x)

# Continue Example
# The 'continue' statement is used to skip the current iteration and move to the next one.
for x in range(10):
    if x == 5:  # If x is equal to 5, skip this iteration
        print("Skipping x =", x)
        continue  # Skips the current iteration and continues with the next one
    print(x)
# Example using both break and continue

# Loop over numbers from 1 to 10
for x in range(1, 11):
    if x == 3:
        print(f"Skipping {x} using 'continue'.")
        continue  # Skip the rest of the code and go to the next iteration when x == 3
    if x == 8:
        print(f"Stopping the loop at {x} using 'break'.")
        break  # Exit the loop completely when x == 8
    print(x)


