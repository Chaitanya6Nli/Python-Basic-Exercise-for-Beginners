# Print the sum of a Current Number and a Previous number

'''
Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
'''

previous_number = 0

for i in range(1, 11):
    sum = previous_number + i
    print("Current Number:", i, "Previous Number:", previous_number, "Sum;", sum)
    previous_number = i