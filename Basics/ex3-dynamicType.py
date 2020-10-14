# Demonstrate dynamic type system in Python

# The variables first and second begin life as one type of variable
first = 1
second = 2.5
print(type(first))
print(type(second))

# Dynamic Type: The variables now become a different type in the same scope
first = "one"
second = [2]
print(type(first))
print(type(second))

malign = True
ma1ign = False

