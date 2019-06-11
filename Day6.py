# 11 June 2019

# BITWISE OPERATOR:      &, |, ^, ~, <<, >>

# 1
a = 10
b = 9
print(a & b)
print(a | b)
print(a ^ b)

# 2
a = -10
b = 9
print(a & b)
print(a | b)
print(a ^ b)

# Bitwise operator between String, float, list, tuple, dictionary are not allowed

# 3
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a & b  # Intersection
a | b  # Union
a ^ b  # Symmetric Difference

# 4
a = -11
~a
a << 2
a >> 2
# ~, >>, << Operators work only on Integer

# IDENTITY OPERATOR:     is, is not

# 1
a = 10
b = 10
a is b

# 2
a = 10.34
b = 10.34
a is b

# MEMBERSHIP OPERATOR        in, in not

# 1
10 in [1, 2, 3, 4, 5]
2 in {1, 2, 3}
1 in {1: "Python", 2: "Java"}
"Python" in {1: "Python", 2: "Java"}
# Membership Operator only checks key in Dictionary, thats why previous line results in false

# OBJECT REFERENCE CREATOR OPERATOR
# 1
a, b = 10, 20
a, b = 10, 20, 30
a, b, c = 10, 20

# 2
a, *b = 1
a, *b = (1,)
a
b

a, *b, c = 1, 2
a
b
c

a, *b, c = 1, 2, 3, 4, 5
a
b
c

*a, *b = 1, 2
