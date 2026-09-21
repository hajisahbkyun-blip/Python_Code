"""
    *
   * *
  * * *
 * * * *
* * * * *

"""


for i in range(1, 6): # loop from 1 to 5
    for j in range(1, 6 - i): # loop from 1 to the current number
        print(" ", end="") # print a space
    for k in range(1, i + 1): # loop from 1 to the current number
        print("*", end=" ") # print a star
    print() # print a new line after each row




    