# Remove first n characters from a string

'''
Write a Python code to remove characters from a string from 0 to n amd return a new string.
'''

def remove_chars(str, n):
    return str[n:]

print(remove_chars("Python", 3))

