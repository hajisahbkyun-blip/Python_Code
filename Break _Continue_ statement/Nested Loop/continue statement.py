# CONTINUE statement

# continue skips the rest of the current iteration 
# and jumps straight to the next one. The loop does not stop – 
# it just skips that particular cycle.

# python
# # continue in a for loop - skip even numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue            # skip even numbers
#     print(i)
# # Output: 1 3 5 7 9

# # continue in a while loop - skip multiples of 3
# num = 0
# while num < 15:
#     num += 1
#     if num % 3 == 0:
#         continue
#     print(num)
# # Output: 1 2 4 5 7 8 10 11 13 14



# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i, end =" ")


# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i, end =" ")