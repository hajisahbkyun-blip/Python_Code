# What is a Conditional Statement?

# In real life, we make decisions based on conditions – "If it is raining, "
# "carry an umbrella, otherwise don't." Python works the same way. 
# A conditional statement lets your program make decisions and execute
# different code based on whether a condition is True or False.


# age = 20

# Program decides what to print based on the value of age
# if age >= 18:
#     print("You are eligible to vote.")



# IF Statement

# The if statement is the most basic form. If the condition is True, 
# the indented block runs. If it is False, Python simply skips it.

# marks = 75

# if marks >= 40:
#     print("You have passed.")

# If marks were 30, nothing would print at all



# IF-ELSE Statement

# Use else when you want something to happen when the condition is False.
# One of the two blocks will always run – never both, never neither.


# age = 16

# if age >= 18:
#     print("You can vote.")
# else:
#     print("You are too young to vote.")



# age = int(input("Enter your age = "))

# if age >= 18:
#     print("You can vote")
#     print("You are responsible voter")
#     print("You are eligbile")
# print("Done")


# age = int(input("Enter your age = "))

# if age >= 18:
#     print("You can vote.")
#     print("You are responsible voter.")
#     print("You are eligbile.")
# else:
#     print("You cannot vote.")


physics = int(input("Enter your physics marks = "))
chemistry = int(input("Enter your chemistry marks = "))

if chemistry > 33 and physics >33 :
    print("Pass")
else:
    print("Fail")