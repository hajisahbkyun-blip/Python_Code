# Operator Precedence

# When multiple operators are in one expression, Python follows a
# order – just like BODMAS in maths.

# Order (highest to lowest):
# ** → Exponentiation
# *, /, //, % → Multiplication & Division
# +, - → Addition & Subtraction


# # Without knowing precedence, this looks confusing
# print(2 + 3 * 4)       # 14, NOT 20 (multiplication first)
# print(10 - 2 ** 3)     # 2, NOT 512 (exponent first)
# print(10 // 2 + 3)     # 8, NOT 1

# # Use parentheses to force the order you want
# print((2 + 3) * 4)     # 20
# print((10 - 2) ** 3)   # 512