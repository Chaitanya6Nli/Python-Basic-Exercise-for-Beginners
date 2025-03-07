# Check if the first and last numbers of a list are the same

'''
Write a code to return True if the list's first and last numbers are the same. If the numbers are different, return False.
'''

def first_last_same(numberList):
    print("Given list is ", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
# Test the function
numbers_x = [10, 20, 30, 40, 10]
print("result is:", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is:", first_last_same(numbers_y))