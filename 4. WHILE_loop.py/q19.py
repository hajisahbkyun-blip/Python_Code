# Q19. Ask a number from the user, and print all the factors.


# num = int(input("Enter the number = "))

# i = 1
# while i <= num:
#     if num % i == 0:
#         print(i, end=" ")
#     i += 1





# Ask a number from the user, and count all the factors.

num = int(input("Enter the number = "))

i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i += 1

print(f"Total factors of {num} = {count}")
