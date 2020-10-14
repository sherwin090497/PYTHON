
print("Hello World!")


#Bounded itereration 

# use the range function to produce a list of sequential integers
for i in range(5):
    print(f"Square {i}: {i*i}")

total = 0
for i in range(1,5):
    total = total + i
    print(f"Running Sum {i}: {total}")

total = 0
for i in range(-5,0):
    total = total + i
    print(f"Running Sum {i}: {total}")

for i in range(0,10,2):
    print(f"Up By Two {i}")

for i in range(10,0,-2):
    print(f"Down By Two {i}")

# Step through the characters IN a string
prompt = "Fett"
for letter in prompt:
    print(letter.upper())

# iterate through all the items in an array (list)
print("Iterate through a list . . .")
data = [1,2,3,25,28,29,37,38]
for item in data:
    if item % 2 == 0:
        print(item)

print("Another way of doing the above")
for item in (x for x in data if x % 2 == 0):
    print(item)