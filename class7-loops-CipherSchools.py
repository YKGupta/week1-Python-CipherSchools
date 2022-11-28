# While loop
a = 1
while a <= 10:
    print(a)
    a += 1

# While loop is used when we don't know how many iterations it will take to produce the required result(generally)

# For loop is used with sequences in python
# Sequences have the attribute __iter__ defined in them (way to identify the same)
# Sequences - string, array, set, tuple, ...
name = "Yash"
for i in name:
    print(i)

for i in range(5):
    print(i)

for i in [1, 5, 6, 7]:
    print(i)
    i = 100

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        print(i)

for i in range(7):
    print(i)
else:
    print("Ended normally")

for i in range(7):
    print(i)
    if (i == 3):
        break
else:
    print("Ended normally")

a = 5
if a == 5:
    # I don't know what to do
    pass
print("end")