# Q4: A student scored marks in 3 subjects. Take all three as input, 
# calculate the total and average, and print both using an f-string.

Chemistry = (int(input("Enter Your Marks in Chemistry = ")))
Biology = (int(input("Enter Your Marks in Biology = ")))
Physics = (int(input("Enter Your Marks in Physics = ")))
total = Chemistry + Biology + Physics
# avg = total/3
avg = (Chemistry + Biology + Physics)/3
# print(f"Total marks = {total} marks and Average marks = {avg}")
print(f"Total marks = {total} marks and Average marks = {avg:.2f}")