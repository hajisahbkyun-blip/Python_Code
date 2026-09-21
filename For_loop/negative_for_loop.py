#  print 10 to 1

# for i in range(10, 0):
#     print(i, end = " ")
# won't give output

# if we are printing 1 to 10 then we are going left to right then step is also (+)
# As we want to print 10 to 1 (we are going right to left as 1,2,3,4,5,5,6,7,8,9,10)
# we going negative so we have to add negative step 



# +ive printing then +ive Step 
# for i in range(10, 0, -1):
    # print(i, end = " ")  won't give output as above 
# -ive printing then -ive step 

# for i in range(10, 0, -1):
#     print(i, end = " ")



for i in range(100, 0, -1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end = " ")