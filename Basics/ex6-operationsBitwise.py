# Bitwise operators in Python. This file also makes extended use of formatted
# strings and Python 3's support for f-strings. This program uses variables 
# entered in as hexidecimal numbers and outputs at least 8 columns. It 
# includes leading zeros 

# enter our data in hex format
first = 0xAA
second = 0xBB

# display the variables in binary format
print("op1: {0:08b}".format(first))
print("op2: {0:08b}".format(second))

# display operation results in binary format
print( f"\nAND: {(first & second):08b}")
print( f" OR: {(first | second):08b}")
print( f"XOR: {(first ^ second):08b}")
print("\nComplete.")