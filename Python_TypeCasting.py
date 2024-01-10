"""
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)


a = float(1)     # x will be 1.0
b = float(2.8)   # y will be 2.8
c = float("3")   # z will be 3.0
d = float("4.2") # w will be 4.2
print(a)
print(b)
print(c)
print(d)



A = str("s1") # x will be 's1'
B = str(2)    # y will be '2'
C = str(3.0)  # z will be '3.0'
print(A)
print(B)
print(C)

