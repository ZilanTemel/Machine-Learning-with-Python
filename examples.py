# Import necessary modules
def manipulate_list():
    # Text transformation and list manipulation
    text = "the goal is to turn data into information ,and information into insight."
    print(text.upper())

    data_list = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
    print(f"Number of elements: {len(data_list)}")
    print("First element:", data_list[0])
    print("Last element:", data_list[-1])
    print("Sublist:", data_list[:4])

    # Modify list
    data_list.append("Z")
    print("List with new element:", data_list)
    data_list.remove(data_list[8])
    print("List without element:", data_list)
    data_list.insert(8, "N")
    print("Modified list:", data_list)

def manipulate_dict():
    # Dictionary manipulation
    my_dict = {
        'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]
    }
    print("Original Dictionary:", my_dict)

    # Update dictionary
    my_dict['Daisy'] = ["England", 13]
    my_dict['Ahmet'] = ["Turkey", 24]
    del my_dict['Antonio']
    print("Updated Dictionary:", my_dict)

def odd_even_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    return odd_numbers, even_numbers

def display_students():
    students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
    eng_students = students[:3]
    med_students = students[3:]

    for idx, student in enumerate(eng_students, start=1):
        print(f"Engineering Student {idx}: {student}")
    for idx, student in enumerate(med_students, start=1):
        print(f"Medical Student {idx}: {student}")

def check_sets(set1, set2):
    if set1.issuperset(set2):
        return set1.intersection(set2)
    return set2.difference(set1)

# Execute functions
if __name__ == "__main__":
    manipulate_list()
    manipulate_dict()

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_nums, even_nums = odd_even_numbers(numbers)
    print("Odd Numbers:", odd_nums)
    print("Even Numbers:", even_nums)

    display_students()

    set1 = set(["data", "python"])
    set2 = set(["data", "function", "qcut", "python", "miuul"])
    print("Set Comparison Result:", check_sets(set1, set2))
