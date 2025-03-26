import math
# string data type

first = "Alan"
last = 'LJ'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

# casting
decade  = str(1980)
print(decade)

# multiple lines
multiline = '''
Hey, how are you?

I was just checking in.   
                    All good?

'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))

print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cake".ljust(16, ".") + "$4".rjust(4))

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# boolean data
print(first.startswith("A"))
print(first.endswith("z"))

# boolean type
myvalue = True
x = bool(False) 

# numeric data types
#int
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
#float
gpa = 3.28
y = float(1.14)

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode = "1001"
zip_value = int(zipcode)
print(type(zip_value))
