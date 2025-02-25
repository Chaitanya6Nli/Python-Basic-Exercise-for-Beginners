# Print the following pattern

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''

rows = 6

# outer loop
for i in range(1, rows):
    # inner loop
    for j in range(i):
        print(i, end=' ')
    print('')