"""
Q3. Take a number as input. Check whether it is even or odd. 
If it is even, print "Even Number". Otherwise, print "Odd Number".

"""

num = int(input("Enter a number: ")) # convert input to integer
if num % 2 == 0: # check if the number is divisible by 2
    print("Even Number")
else:
    print("Odd Number")