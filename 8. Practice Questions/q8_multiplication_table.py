"""
Q8. Take a number as input. Print its multiplication table
 from 1 to 10 using a for loop.

"""
num = int(input("Enter a number: ")) # take input from the user
for i in range(1, 11): # loop from 1 to 10
    print(f"{num} x {i} = {num * i}") # print the multiplication table  
    