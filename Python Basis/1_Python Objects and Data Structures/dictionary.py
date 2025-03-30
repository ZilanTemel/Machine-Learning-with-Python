
# 1. What is a Dictionary?
# A dictionary is a data structure that works with key-value pairs.
# It is defined inside curly braces {} and key-value pairs are separated by commas.

# Example dictionary:
person = {
    "name": "Zilan",
    "age": 25,
    "profession": "Computer Engineer",
    "languages": ["Python", "Java", "C"]
}

# 2. Accessing Dictionary Elements
print("Name:", person["name"])  # "Zilan"
print("Age:", person.get("age"))  # 25
print("Profession:", person.get("profession", "Unknown"))  # "Computer Engineer"
print("Known Languages:", person["languages"])  # ["Python", "Java", "C"]

# 3. Adding a New Key-Value Pair
person["city"] = "Istanbul"
print("\nUpdated Dictionary:", person)

# 4. Updating an Existing Key
person["age"] = 26
print("\nAge Updated:", person)

# 5. Deleting a Key
del person["profession"]
print("\nProfession Key Removed:", person)

# 6. Listing All Keys and Values
print("\nKeys:", list(person.keys()))
print("Values:", list(person.values()))
print("Key-Value Pairs:", list(person.items()))

# 7. Creating a Dictionary with User Input
print("\nCreate Your Own Dictionary!")
new_person = {}
new_person["name"] = input("Enter your name: ")
new_person["age"] = int(input("Enter your age: "))
new_person["city"] = input("Enter your city: ")

print("\nYour Created Dictionary:", new_person)

# 8. Using Loops in a Dictionary
print("\nDictionary Contents:")
for key, value in new_person.items():
    print(f"{key}: {value}")

# 9. Using Default Values with the get() Method
country = new_person.get("country", "Unknown")
print("\nCountry:", country)

# 10. Copying a Dictionary (Shallow Copy)
copy_person = new_person.copy()
print("\nCopied Dictionary:", copy_person)
