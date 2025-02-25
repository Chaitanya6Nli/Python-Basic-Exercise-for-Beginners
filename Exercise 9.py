# Check Palindrome Number

'''
Write a Python code to check if the given number is palindrome.

A Palindrome number is a number that remains the same when its digits are reversed.

For example, 121, 1331, 12321, etc.
'''

# Function to check if the given number is palindrome
def is_palindrome(num):
    print("Original Number: ", num)
    original_num = num

    # Reverse the number
    reverse_num = 0
    while num > 0: # Loop until num is greater than 0
        remainder = num % 10 # Extract the last digit
        reverse_num = (reverse_num * 10) + remainder # Append the last digit to reverse_num
        num = num // 10 # Remove the last digit from num

    # check numbers
    if original_num == reverse_num:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")

# Test the function
is_palindrome(121)
is_palindrome(125)

# # Input number
# num = int(input("Enter a number: "))
# is_palindrome(num) # Function call
