# Shorthand if-else (Ternary Operator)

# Python lets you write a simple if-else in a single line.
# This is called the ternary operator. It is useful when you want
# to assign a value based on a condition.


# # Normal way
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# # Shorthand way (same result, one line)
# status = "Adult" if age >= 18 else "Minor"
# print(status)



age = int(input("Enter you age = "))

# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

status = "Adult" if age >=18 else "Minor"

print(f"Your status is {status}.")