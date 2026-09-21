# NESTED IF-ELSE Statement

# You can place an if statement inside another if statement. 
# This is called nesting and is useful when a second condition 
# only makes sense if the first one is already True.


# age = int(input("Enter you age = "))
# has_degree = True

# if age >= 18:
#     print("Age requirement met.")
#     if has_degree:
#         print("You are eligible for this job.")
#     else:
#         print("You need a degree for this job.")
# else:
#     print("You are too young to apply.")

# age >= 18
# certificate -> True 


# age = 45
# certificate = True
# if age >=18:
#     if certificate == True:
#         print("You will be hired")
#     else:
#         print("You need a certficate for this post")
# else:
#     print("You are too young for this post")




age = int(input("Enter your age: "))
cert_input = input("Do you have the required Certificate? (yes/no): ").lower()
certificate = (cert_input == "yes")

if age >= 18:
    if certificate == True:
        print("You will be hired.")
    else:
        print("You need a certifircate for this post")
else:
    if certificate == True:
        print("You are too young for this post")
    else:
        print("You are too young and also need the certificate.")

        