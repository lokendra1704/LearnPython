# 1
a = int()
type(a)
a
id(a)

# 2
a = int(10)
id(a)

# 3
a = 256
b = 256
id(a)
id(b)  # IDs of integers are same in range [-5,256]

# 4
a = 257
b = 257
id(a)
id(b)

# 5
a = -6
b = -6
id(a)
id(b)

# 7
a = float(10.34)
b = float(10.34)  # same as b=10.34
id(a)
id(b)  # IDs of float (even with same values) will always be different

# 8
a = 10 + 20j
type(a)
b = 10 + 20j
id(a)
id(b)  # IDs of Complex (even with same values) will always be different

# 9
a = "hello"  # same as a='hello'
b = "hello"
id(a)
id(b)  # IDs of string will be same when no collection occurs

# 10
a = "a b"
b = "a b"
id(a)
id(b)  # IDs of string are different when collection occurs
