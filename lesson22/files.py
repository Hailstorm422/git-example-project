import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesnt exist

f = open("names.txt", "r") #"rt" = read text file, "rb" = read binary
#print(f.read())
#print(f.read(4)) #4 characters
#print(f.readline()) #read a line
#print(f.readline()) #read a line

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesnt exist.")
finally:
    f.close()

# Append - creates the file id it doesnt exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to creat a new file
# Opens a file for Writing, creates if it doesnt exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
#avoid an error if it doesnt exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete doesnt exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)



