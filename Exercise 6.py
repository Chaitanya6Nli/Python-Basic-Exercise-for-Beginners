# Display numbers divisible by 5

'''
Write a Python code to display numbers from a list divisible by 5
'''

# List of numbers
num_list = [10, 20, 33, 46, 55]
print("Given list of numbers:", num_list)

# Display numbers divisible by 5
print("Numbers divisible by 5:")

for num in num_list:
    if num % 5 == 0:
        print(num)