from PyQt5.uic.properties import int_list
from decorator import append
from docutils.nodes import definition_list_item
from fontTools.misc.cython import returns
from numba.core.ir import Print
from pygments.lexer import combined
from sympy.integrals.rubi.parsetools.parse import seperate_freeq
from xlwings.mac_dict import classes

text="the goal is to turn data into information ,and information into insight."

result=text.upper(),
print(result)

list=["D","A","T","A","S","C","I","E","N","C","E"]

nuberOfElements=len(list)
print(nuberOfElements)
print(list[0])
print(list[10])
minList=list[0:4]
print("New List :",minList)
list.append("Z")
print("List with new element",list)
list.remove(list[8])
print("List without an elment",list)
list.insert(8,"N") # The `list.append()` method only takes one argument, so `list.append(8, "N")` is incorrect; use `list.insert(index, element)` instead.

print(list)

dict={'Christian' : ["America",18],
     'Daisy':["England",12],
     'Antonio ':["Spain",22],
     'Dante':["Italy",25]}
keys=dict.keys()
print("Keys:",keys)
values=dict.values()
print("Values:",values)

dict['Daisy']=["England",13]
print("updated dict:",dict)
dict['Ahmet']=["Turkey",24]
print("New dict:",dict)
del dict['Antonio ']
print("New list:",dict)
###########################################################################

# Function to get odd numbers
def odd_numbers(lst):
    odd_nums = []
    for number in lst:
        if number % 2 != 0:
            odd_nums.append(number)
    return odd_nums

# Function to get even numbers
def even_numbers(lst):
    even_nums = []
    for number in lst:
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums

# Example numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the functions
odd_nums = odd_numbers(numbers)
even_nums = even_numbers(numbers)

# Print the results
print("Odd Numbers:", odd_nums)
print("Even Numbers:", even_nums)

#####################################################
students=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

engineering_students=students[:3]

medical_students=students[3:]

for index,student in enumerate(engineering_students,start=1):
    print(f"Engineering Faculty {index}.student :{student}")
for index,student in enumerate(medical_students,start=1):
    print(f"Medical Faculty {index}.student:{student}")

##########################################################

class_code=["CMP1005","PSY1001","HUK1005","SEN284"]
credits=[3,4,2,4]
capacities=[30,75,150,25]

combinated=zip(credits,class_code,capacities)

for credit,code,capacity in combinated:
    print(f"The course with code {code} has a credit of {credit} and a capacity of {capacity} students.")

######################################################################################################################

def check_sets(set1,set2):
    if set1.issuperset(set2):
        return set1.intersection(set2)
    else:
        return set2.difference(set1)

set1=set(["data","python"])
set2=set(["data","function","qcut","python","miuul"])

result=check_sets(set1,set2)
print(result)












