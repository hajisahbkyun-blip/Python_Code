# Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100.

i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1