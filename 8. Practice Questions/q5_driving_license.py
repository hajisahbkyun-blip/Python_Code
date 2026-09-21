"""
Q5. Take a user's age and whether they have a driving license (yes/no) as input.

If age is 18 or above AND they have a license, print "You can drive."

If age is below 18, print "You are too young to drive."

If age is 18 or above but they do not have a license, print "You need a license."

"""

age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ").strip().lower() # convert input to lowercase and remove any leading/trailing whitespace

if age >= 18:
    if license == "yes":
        print("You can drive.")
    else:
        print("You need a license.")
else:
    print("You are too young to drive.")