# Q12: Take three numbers as input. Print the largest of the 
# three without using any built-in function.


num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))
num3 = int(input("Enter num3 = "))
if num1 >= num2 and num1 >= num3:
    print("Largest number is Num1 ")
    # largest = num1
elif num2 >= num1 and num2 >= num3:
    print("Largest number is Num2 ")
    # largest = num2
else:
    print("Largest number is Num3 ")
    # largest = num3
# print("Largest number is =", largest)
