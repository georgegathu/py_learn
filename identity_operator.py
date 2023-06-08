"""
# Identity Operators
This includes:
    a) is    (This returns True if both variables are the same object)
    b) isnot (This returns True if both variables are not the same object)
They are used to compare objects: If they are the same or not and they share same memory location
"""

# Example 1 (is Operator)
x = 5
y = 5

print(x is y) # True

# Example 2 (is not Operator)
x = 5
y = 5

print(x is not y) # False

# Example 3:
x = 5
y = "5"
print(x is y) # False

x = 5
y = "5"
print(x is not y) # True

#TEST:
x = 5
print(id(x))

x = 8
print(id(x))

print(x is x ) # True
