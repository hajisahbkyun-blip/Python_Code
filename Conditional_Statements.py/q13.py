# Q13: Take a number as input. Using the ternary operator, 
# print "Even" or "Odd" in a single line.

number = int(input("Enter the number = "))
check = "Even" if number % 2 == 0 else "Odd"
print(check)