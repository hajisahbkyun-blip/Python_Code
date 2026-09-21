"""
Q15. Take 10 numbers as input using a loop. Calculate and print 
the sum of only the positive numbers. Skip any negative numbers.

"""

sum_positive = 0
for i in range(1,11): # loop 10 times
    num = int(input(f"Enter number {i}: ")) # take input from the user
    if num < 0: # check if the number is negative
        continue # skip the current iteration if it is negative
    sum_positive += num # add the positive number to the sum    
print(f"The sum of all positive numbers = {sum_positive}.") # print the result