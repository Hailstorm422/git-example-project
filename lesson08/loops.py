value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else: # does not execute on break
    print("value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)
for x in names:
     if x == "Sara":
         break
     print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)
    
for x in range(4):
    print(x)

for x in range(2,4):
    print(x)

for x in range(5,101,5):
    print(x)
else:
    print("Done")

actions = ["codes", "eats", "sleeps"]
for name in names:
    for action in actions:
        print(name + " " + action + ".")



