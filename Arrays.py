from array import *

numbers = array('i', [10, 20, 30, 40, 50])

def display(array):
    for x in array:
        print(x)

# Printing all elements
print("Printing all elements of array:")
display(numbers)
print("")

# Accessing elements
print("Accessing 10 and 30: ")
print(numbers[0])
print(numbers[2])
print("")

# Inserting
print("Inserting 60:")
numbers.insert(5, 60)
display(numbers)
print("")

# Deleting 40
print("Deleting 40 from array:")
numbers.remove(40)
display(numbers)
print("")

# Search for 30
print("Searching for 30 in the array:")
print(numbers.index(30))
print("")

# Updating 20
print("Updating 20 to 40:")
numbers[numbers.index(20)] = 40
display(numbers)
