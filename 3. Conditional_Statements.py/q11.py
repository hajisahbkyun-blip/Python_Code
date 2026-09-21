# Q11: Take a person's age and whether they have a valid ID (True/False) as input. 
# They can enter a venue only if they are 18 or older AND have a valid ID.
# Print the appropriate message.


your_age = int(input("Enter your age = "))
valid_id = bool(input("Do you have a valid ID (True/False) : "))
okay =(valid_id == True)

if your_age >= 18 and valid_id == okay:
    print("You can enter a venue.")
else:
    print("You can not enter a venue.")
