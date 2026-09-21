# Q20. Count all the numbers from 1 to 100 divisible by 2 and 7.

i = 1
count = 0
while i <=100:
    if i % 2 == 0 and i % 7 == 0:
        count = count + 1
    i += 1 
print(f"Total numbers divisible by 2 and 7 = {count}")