# Creating a String----------------------------

# Single word
print('hello')

# Entire phrase
print('This is also a string')

# We can also use double quotes
print("String built with double quotes")

# When using an apostrophe use double quotes
print("Now I'm ready to use the single quotes inside a string")

# Built in function to get the length of a string
print(len('Hello'))

# String Indexing------------------------------

# Assign a as a string
s = 'Hello World'

# Print the object
print(s)

# Show the first element(in this case a letter)
print(s[0])
print(s[1])
print(s[2])

# String slicing-------------------------------

# Grab everything past the first term all the wqay to the length of s which is len(s)
print(s[1:])

# Note that there is no change to the original s
print(s)

# Grab everything UP TO the 3rd index
print(s[:3])

# Grab everything
print(s[:])

# Grab the last letter (one index behind 0 so it loops around)
print(s[-1])

# Grab everything but the last letter
print(s[:-1])

# Grab everything, but go in step sizes of 2
print(s[::2])

# We can use this to print a string backwards
print(s[::-1])

# String Properties----------------------------

# Let's try to change the first letter to 'x'
# s[0] = 'x' This will give you an error since strings are immutable

# Concatenate strings!
print(s + ' concatenate me!')

# We can reassign s completely
s = s + ' concatenate me!'
print(s)

# We can use the multiplication symbol to create repetition
letter = 'z'
print(letter*10)

# Basic Built-in String methods----------------

# Upper Case a string
print(s.upper())

# Lower case
print(s.lower())

# Split a string  by blank space (this is the default)
print(s.split())

# Print Formating------------------------------
name = 'William'
print(f'Hello {name}')
print('Hello {}'.format(name))
