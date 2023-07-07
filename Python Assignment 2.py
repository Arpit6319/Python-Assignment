# Arithmetic operators
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
exponentiation = a ** b
floor_division = a // b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
print(f"Floor Division: {floor_division}")

# Comparison operators
x = 5
y = 7

greater_than = x > y
less_than = x < y
equal_to = x == y
not_equal_to = x != y
greater_than_or_equal_to = x >= y
less_than_or_equal_to = x <= y

print(f"Greater than: {greater_than}")
print(f"Less than: {less_than}")
print(f"Equal to: {equal_to}")
print(f"Not equal to: {not_equal_to}")
print(f"Greater than or equal to: {greater_than_or_equal_to}")
print(f"Less than or equal to: {less_than_or_equal_to}")

# Logical operators
p = True
q = False

logical_and = p and q
logical_or = p or q
logical_not = not p

print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT: {logical_not}")

# Bitwise operators
m = 8
n = 3

bitwise_and = m & n
bitwise_or = m | n
bitwise_xor = m ^ n
bitwise_not = ~m
bitwise_left_shift = m << n
bitwise_right_shift = m >> n

print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Bitwise Left Shift: {bitwise_left_shift}")
print(f"Bitwise Right Shift: {bitwise_right_shift}")

# Assignment operators
x = 10

x += 5
print(f"Add and Assign: {x}")

x -= 3
print(f"Subtract and Assign: {x}")

x *= 2
print(f"Multiply and Assign: {x}")

x /= 4
print(f"Divide and Assign: {x}")

x %= 3
print(f"Modulus and Assign: {x}")

x //= 2
print(f"Floor Divide and Assign: {x}")

x **= 3
print(f"Exponentiation and Assign: {x}")

# Identity operators
a = "Hello"
b = "World"
c = "Hello"

print(f"Is 'a' the same as 'b'?: {a is b}")
print(f"Is 'a' not the same as 'b'?: {a is not b}")
print(f"Is 'a' the same as 'c'?: {a is c}")

# Membership operators
list_numbers = [1, 2, 3, 4, 5]

print(f"Is 3 in the list?: {3 in list_numbers}")
print(f"Is 6 not in the list?: {6 not in list_numbers}")