# Q20. Take numbers as input from the user one by one. 
# Skip negative numbers and keep adding the positive ones. 
# Stop when the user enters 0 and print the total. (Uses both continue and break.)

total = 0
while True:
    num = int(input("Enter number = "))
    if num < 0:
        continue
    if num > 0:
        total += num
    if num == 0:
        break
print(f"total = {total}")

