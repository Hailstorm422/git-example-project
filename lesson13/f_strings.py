person = "Dave"
coins = 3
#1
print("\n" + person + " has " + str(coins) + " coins left.")
#2
message = "\n%s has %s coins left." % (person, coins)
print(message)
#3
message = "\n{} has {} coins left.".format(person, coins)
print(message)
#4
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)
#5
message = "\n{person} has {coins} coins left.".format(coins = coins, person = person)
print(message)

#6
player = {'person': "Dave", 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

##################
# f-strings
#7
message = f"\n{person} has {coins} coins left."
print(message)
#8
message = f"\n{person} has {2 * 5} coins left."
print(message)
#9
message = f"\n{person.lower()} has {coins} coins left."
print(message)
#10
message = f"\n{player['person']} has {coins} coins left."
print(message)

#################
# you can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")


