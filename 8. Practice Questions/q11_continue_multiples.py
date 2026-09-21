"""
Q11. Print numbers from 1 to 20, but skip (continue) the multiples of 5 (5, 10, 15, 20).

"""

for i in range(1, 21): # loop from 1 to 20
    if i % 5 == 0: # check if the number is a multiple of 5
        continue # skip the current iteration if it is a multiple of 5
    print(i, end=" ") # print the current number
        