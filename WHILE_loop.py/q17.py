# Q17. Sum of all the numbers from 1 to 100 divisible by 2 and 7.


# i = 1
# total = 0
# while i <=100:
#     if i % 2 == 0 and i % 7 == 0:
#         total = total + i
#     i += 1
# print(f"Total = {total}")




start = int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))

i = start
total = 0
while i <=end:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1
print(f"Total = {total}")