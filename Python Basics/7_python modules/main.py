import Mymodule

print("Number:", Mymodule.number)
print("Numbers list:", Mymodule.numbers)
print("Person name:", Mymodule.person["name"])
print("Person age:", Mymodule.person["age"])
print("Function output (10 * 2):", Mymodule.func(10))

elif_woman = Mymodule.Woman(Mymodule.person["name"])
elif_woman.speak()
