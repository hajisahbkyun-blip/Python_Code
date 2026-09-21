# Q6: Take two numbers as input. Without using *, calculate and 
# print their product using += in a way that adds the first number
# to itself the second number of times.

num1 = int(input("Enter the num1 = ")) 
num2 = int(input("Enter the num2 = "))
result = 0
for i in range(num2):
    result+=num1

print("Product = ",result)
