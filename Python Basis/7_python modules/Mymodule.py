number = 42
numbers = [1, 2, 3, 4, 5]
person = {
    "name": "Elif",
    "age": 28,
    "gender": "female"
}

def func(x):
    return x * 2
class Woman:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hello, I'm {self.name} and my voice matters.")

# main.py
import Mymodule

print("Number:", Mymodule.number)
print("Numbers list:", Mymodule.numbers)
print("Person name:", Mymodule.person["name"])
print("Person age:", Mymodule.person["age"])
print("Function output (10 * 2):", Mymodule.func(10))

# Create a Woman instance using the person object
elif_woman = Mymodule.Woman(Mymodule.person["name"])
elif_woman.speak()
