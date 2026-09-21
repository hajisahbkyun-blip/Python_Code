# Q14: A shop gives discounts based on purchase amount:

# Above 5000 → 20% discount

# Above 2000 → 10% discount

# Above 1000 → 5% discount

# 1000 or below → no discount



amount = int(input("Enter ammount = "))
if amount > 5000:
    print("20% discount")
elif amount > 2000 and amount <= 5000:
    print("10% discount")
elif amount > 1000 and amount <= 2000:
    print("5% discount")
else:
    print("No discount")
