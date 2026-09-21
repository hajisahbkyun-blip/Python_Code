"""
Q10. Print numbers from 1 to 100, but stop (break) 
the loop when the number reaches 50.

"""

for i in range(1, 101): # loop from 1 to 100
    if i == 50: # check if the number is 50
        break # break the loop if the number is 50
    print(i, end=" ") # print the current number

