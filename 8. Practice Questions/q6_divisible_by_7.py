"""
Q6. Print all numbers from 1 to 50 that are divisible by 7 using a while loop.

"""


i = 1 
while i <= 50: 
    if i % 7 == 0: # check if the number is divisible by 7
        print(i, end = " ") # print the number followed by a space
    i += 1  

