# Calculate area and circumference of a circle given the radius

pi = 3.14
r = float(input("Enter radius: "))

circumference = 2 * pi * r
area = pi * (r ** 2)

print("Circumference:", circumference)
print("Area:", area)
