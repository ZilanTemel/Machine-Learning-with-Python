# Class Definition: A blueprint for creating Person objects.
class Person:
    # Class attribute: shared by all instances of the class.
    address = 'no information'  # All persons initially have the same address value.

    # Constructor (initializer method) is called when a new object is created.
    def __init__(self, name, year):
        # Instance attributes: unique for each object.
        self.name = name  # Assigns the 'name' to the instance.
        self.year = year  # Assigns the 'year' to the instance.
        print('Constructor called.')  # This will print when the constructor is called (when a new object is created).

# Creating objects (instances) of the Person class.
p1 = Person(name='Aleyna', year=2006)  # Creating a Person object 'p1' with name 'Aleyna' and year 2006.
p2 = Person(name='Eren', year=2003)  # Creating another Person object 'p2' with name 'Eren' and year 2003.

# Updating the attributes of the objects
p1.name = 'Sametcan'  # Changing 'p1' name from 'Aleyna' to 'Sametcan'.
p1.address = 'Van'  # Changing the 'address' of 'p1'. Note: even though 'address' is a class attribute, we can change it for 'p1' only.

# Accessing and printing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')  # Prints p1's attributes after update.
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')  # Prints p2's attributes.

# Printing the objects directly. This will show the object references/memory locations.
print(p1)  # Prints the memory reference of the p1 object.
print(p2)  # Prints the memory reference of the p2 object.
