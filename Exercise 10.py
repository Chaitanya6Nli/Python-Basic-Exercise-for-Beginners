# Merge two lists using the following conditions:

'''
Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
'''

# Define the two lists
list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

# Define the new list
list3 = []

# Loop through the first list
for x in list1:
    if x % 2 != 0:
        list3.append(x)

# Loop through the second list
for x in list2:
    if x % 2 == 0:
        list3.append(x)

# Print the new list
print(list3)
