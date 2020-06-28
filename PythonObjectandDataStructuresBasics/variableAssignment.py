# Let's create an object called "a" and assign it the number 5
a = 5

# Adding the objects
print(a+a)

# Reassignment
a = 10
print(a)

# Use A to redefine A
a = a + 10
print(a)

# Shortcut for math operations with reassignments
a += 10
print(a)
a *= 2


# Checking type
print(type(a))

a = (1, 2)

print(type(a))
"""
Variables Naming conventions
1. Names can't start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols:'",<>/?|\()!@#$%^&*~-+
4. It's considered best practices (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 
'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single
character variable names.
6. Avoid ysubg words that hace special meaning in Python like "list" and "str".

"""

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)
