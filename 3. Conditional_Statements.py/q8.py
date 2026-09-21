# Q8: Take two numbers as input. Print the greater of the two. If they are equal, 
# print "Both are equal."

num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))
if num1 > num2:
    print("Number 1 is greater than num2.")
    if num1 < num2:
        print("Num2 is greater than num1.")
else:
    print("Both are equal.")