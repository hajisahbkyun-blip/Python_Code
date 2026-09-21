# Ask start and end, print start to end

# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))

# # for i in range(start, end):
# for i in range(start, end + 1):
#     print(i, end=" ")



# Ask start and end, print sum of all numbers


# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))


# sum = 0
# for i in range(start, end + 1):
#     print(i, end=" ")
#     sum = sum + i
# print(f"\nSum of numbers = {sum}")



# Print 1 to n, where n is the number input by user.

# n =int(input("Enter the number = "))

# i = 1

# for t in range (i, n + 1):
#     print(i, end =" ")
#     i += 1




#  start and end by user
# start to end print using for loop

# example:
# start=6
# end=10
# print 6 to 10


# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))

# for i in range(start, end + 1):
#     print(i, end = " ")
#     i += 1



# Ask start and end from User and print from end to star.
# Start 1
# end 10
# print 10 to 1

# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))

# for i in range (end,start - 1, -1):
#     print(i, end = " ")




# Ask start and end print even numbers.

# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))

# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i, end = " ")






# print start to end (from user), number is divisible by 3 and 4.

# start = int(input("Enter the starting number = "))
# end = int(input("Enter the ending number = "))

# for i in range(start, end + 1):
#     if i % 3 == 0 and i % 4 == 0:
#         print(i, end = " ")



# Ask a number from the user, print the multiplication table upto 10.
#  kisi bhi number ka table banana likhna hai jo user inout krega.


# num = int(input("Enter the starting number = "))
# i = 1
# for t in range(i, 10 + 1):
#     product = num * i
#     print(f"{num} x {i} = {product}")
#     i += 1
    


#  Ask a number from the user, and print all the factors.


num = int(input("Enter the number = "))
i = 1
for t in range(i, num + 1):
    if num % i == 0:
        print(i, end = " ")
    i += 1
