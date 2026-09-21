"""

Q1. Take a user's name, age, and city as input. Print them in the following format:
My name is Ali, I am 20 years old, and I live in Lahore.

"""

# Taking user input for name, age, and city
name = input("Enter your name: ").title() # Capitalize the first letter of each word in the name

age = int(input("Enter your age: "))  # Convert age to integer
city = input("Enter your city: ").title()

# Printing the formatted output
print(f"My name is {name}, I am {age} years old, and I live in {city}.")