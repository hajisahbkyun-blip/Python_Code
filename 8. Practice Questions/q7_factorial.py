"""
Q7. Take a number as input. Calculate and print its factorial using a while loop.
Example: If the number is 5, then 5 * 4 * 3 * 2 * 1 = 120.

"""

num = int(input("Enter a number: ")) # take input from the user
factorial = 1 # initialize factorial to 1
i = 1 # initialize counter to 1
while i <= num: # loop until i is less than or equal to the input number
    factorial *= i # multiply factorial by the current value of i
    i += 1 # increment the counter  
print(f"The factorial of {num} is {factorial}.") # print the result