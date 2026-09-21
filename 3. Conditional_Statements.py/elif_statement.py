# IF-ELIF-ELSE Statement

# When you have more than two possible outcomes, use elif (short for "else if"). 
# Python checks each condition from top to bottom and runs the first one that is True.
# The rest are skipped entirely.


# marks = 82

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("Grade: F")





# 90 aobve -> A
# 81 - 90 -> B 
# 71 - 80 -> C 
# 61 - 70 -> D 
# 60 or below -> F 

# marks = int(input("Enter your marks = "))

# if marks >= 91:
#     print("Grade: A")
# elif marks >= 81 and marks <= 90:
#     print("Grade: B")
# elif marks >= 71 and marks <= 80:
#     print("Grade: C")
# elif marks >= 61 and marks <= 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# marks = int(input("Enter your marks = "))

# if marks >= 91 and marks <= 100:
#     print("Grade: A")
# elif marks >= 81 and marks <= 90:
#     print("Grade: B")
# elif marks >= 71 and marks <= 80:
#     print("Grade: C")
# elif marks >= 61 and marks <= 70:
#     print("Grade: D")
# elif marks >= 0 and marks <= 60:
#     print("Fail")
# else:
#     print("Invalid Input")