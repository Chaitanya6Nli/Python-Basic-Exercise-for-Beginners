# Get each digit from a number in the reverse order

'''
For example, if the input is 12345, the output should be 5, 4, 3, 2, 1
'''

number = int(input("Enter a number:"))

while number > 0:
    # Get the last digit
    digit = number % 10
    # remove the last digit and repeat the process
    number = number // 10
    print(digit, end=", ")