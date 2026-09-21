"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

for i in range(1, 6): # loop from 1 to 5
    for j in range(1, i + 1): # loop from 1 to the current number
        print(i, end=" ") # print the current number
    print() # print a new line after each row


