# print start to end, number is divisible by 3 and 4.

start = int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
    i += 1