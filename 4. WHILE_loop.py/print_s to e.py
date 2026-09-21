#  start and end by user
# start to end print using while loop

# example:
# start=6
# end=10
# print 6 to 10

start = int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))

i = start
while i <= end:
    print(i, end=" ")
    i += 1
print(f"After while loop, start number is {start}")