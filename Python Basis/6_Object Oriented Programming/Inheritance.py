# 🟢 Inheritance - Object-Oriented Programming (OOP) Concept
# Inheritance allows child classes to inherit attributes and methods from a parent class.
# This helps reduce code duplication and makes the program more modular.

# Parent Class: Instrument (Base Class)
class Instrument:
    def __init__(self, brand, model, year):
        # Initializing common attributes for all instruments
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Instrument Created: {self.brand} {self.model} ({self.year})")

    def play(self):
        """A general method for all instruments - playing the instrument."""
        print(f"Playing {self.brand} {self.model}...")

    def stop(self):
        """A general method for stopping the instrument."""
        print(f"Stopped playing {self.brand} {self.model}.")

    def who_am_i(self):
        print("I am an instrument")

#  Child Class: Violin (Inherits from Instrument)
class Violin(Instrument):
    def __init__(self, brand, model, year, strings):
        super().__init__(brand, model, year)  # Calls the parent class constructor to initialize common attributes
        self.strings = strings  # Number of strings on the violin
        print(f"Violin Created: {self.brand} {self.model} ({self.year}) - {self.strings} strings")

    def who_am_i(self):
        """Overrides the parent class method to provide specific behavior for violins."""
        print(f"I am a violin: {self.brand} {self.model}")

    def tune(self):
        """A method specific to violins - tuning the violin."""
        print(f"Tuning the violin: {self.brand} {self.model}")

# Child Class: Guitar (Inherits from Instrument)
class Guitar(Instrument):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)  # Calls the parent class constructor to initialize common attributes
        self.type = type  # Type of guitar (Acoustic, Electric, etc.)
        print(f"Guitar Created: {self.brand} {self.model} ({self.year}) - {self.type}")

    def who_am_i(self):
        """Overrides the parent class method to provide specific behavior for guitars."""
        print(f"I am a guitar: {self.brand} {self.model}")

    def strum(self):
        """A method specific to guitars - strumming the strings."""
        print(f"Strumming the guitar: {self.brand} {self.model}")

# Creating Objects (Instances)
inst1 = Instrument("Generic", "ModelX", 2022)
v1 = Violin("Stradivarius", "Classic", 2023, 4)
g1 = Guitar("Fender", "Stratocaster", 2022, "Electric")

#Usage: Demonstrating the use of methods from the parent and child classes
inst1.who_am_i()  # Output: I am an instrument
v1.who_am_i()  # Output: I am a violin: Stradivarius Classic  (Overridden)
g1.who_am_i()  # Output: I am a guitar: Fender Stratocaster  (Overridden)
inst1.play()  # Output: Playing Generic ModelX...
v1.play()  # Output: Playing Stradivarius Classic...
g1.play()  # Output: Playing Fender Stratocaster...
inst1.stop()  # Output: Stopped playing Generic ModelX.
v1.stop()  # Output: Stopped playing Stradivarius Classic.
g1.stop()  # Output: Stopped playing Fender Stratocaster.
v1.tune()  # Output: Tuning the violin: Stradivarius Classic (Specific to Violin)
g1.strum()  # Output: Strumming the guitar: Fender Stratocaster (Specific to Guitar)

