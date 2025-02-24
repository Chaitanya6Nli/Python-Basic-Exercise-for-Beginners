# Print characters present at an even index number.

'''
Write a Python code to accept a string from the user and display the characters present at an even index number.
'''

# Accepting the string from the user
string = input("Enter a string : ")

# Displaying the characters present at an even index number
print("Characters present at an even index number are:")

for i in range(0, len(string), 2):
    print(string[i], end=" ")