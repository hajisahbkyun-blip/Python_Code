# Q9: Take a student's marks as input. Print their grade based on this scale:

# 90 and above → A
# 75 to 89 → B
# 60 to 74 → C
# 40 to 59 → D
# Below 40 → F


marks = int(input("Enter you marks = "))
if marks >=90 and marks <= 100:
    print("Grade A")
elif marks >=75 and marks <= 90:
    print("Grade B")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 40 and marks <= 59:
    print("Grade D")
elif marks == 0 and marks < 40:
    print("Fail")
else:
    print("Invalid Input")
