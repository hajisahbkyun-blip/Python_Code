# Q18. Ask a number from the user, print the multiplication table upto 10.
#  kisi bhi number ka table banana likhna hai jo user inout krega.


num = int(input("Enter the number = "))

i = 1
while i <=10:
    product = num * i
    print(f"{num} x {i} =", product)
    i += 1
