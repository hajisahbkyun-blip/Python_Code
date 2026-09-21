"""
Q4. Take a number as input. Check whether it is positive, negative, or zero.

If positive, print "Positive"

If negative, print "Negative"

If zero, print "Zero"

"""
num = float(input("Enter a number: ")) # convert input to float to handle decimal numbers
if num > 0: # check if the number is greater than 0
    print("Positive")  
elif num < 0: # check if the number is less than 0
    print("Negative")
else: # if the number is neither greater than nor less than 0, it must be
    print("Zero")