Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Numeric Data Types

# ints - interger, number, just like in math: 1,23,-1,-2,-3,0,500,1000
#floats - decimals numbersL 1.9,3.7,1.7,2.0

# 2 vs 2.0 vs 2. : Python sees 2 as the int, 2 but it sees 2.0 and 2. as the floats, 2.0 and 2.

# Strings - sequences of characters: 'A13', 'Hello, World', '4'. Strings are denoted with single quotes. Technically, you can get away with double quote, and occasionally double quotes are needed, but professional python style is to prioritize.

# Each character in a string has a position (aka an index). THe first character's index is 0. The next character's is 1, etc.
# For example, the 0th character is 'Hello, World' is H.
# The 6th character in 'Hello, World' is a space.

# Operations:

# + means add with ints:

print(2 + 3)

# + means add floats:

print (2.0 + 1.5)

# + means add when combining an int and a float: When Python adds an int to  a float, the result is a float.:
print(2 + 3.0)

# + means ___ when combining strings.
print('Computer' + 'Science')
print('10' + '5')

# Try to combine an int and a string with +?

# + means ___ when combining multiplication when combining ints and floats with each other , but it means repitition when combining ints with a string:
# When combining ints with floats, the float is prioritized. In other words, the result is a float.
print(2 * 5)
print(2. * 5)
print(2 * '5')
print('5' * 2)

# Divisions of floats and ints:
print(10/2)
print(10./2.)
print(10/2.)
print(10./2)

# Float division: /
# Int Division: //

print(10//2)
print(10//2.)
print(10.//2)
print(10.//2.)

print(7//3)
print(5.//2.)


