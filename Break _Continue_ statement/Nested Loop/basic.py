# Nested Loops

# A nested loop is a loop inside another loop.
# The inner loop completes all its iterations
# for every single iteration of the outer loop.


# for outer in range(1, 4):
#     for inner in range(1, 4):
#         print(f"outer={outer}, inner={inner}")

# Output:
# outer=1, inner=1
# outer=1, inner=2
# outer=1, inner=3
# outer=2, inner=1
# outer=2, inner=2
# outer=2, inner=3
# outer=3, inner=1
# outer=3, inner=2
# outer=3, inner=3

for i in range(1,4):
    print(f"i = {i}")
    for j in range(10,14):
        print(f"j = {j}")
print("Done!")