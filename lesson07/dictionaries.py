# dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
    }

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# removing items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries
# band2 = band #creates a reference
# print("Bad copy")
# print(band)
# print(band2)

# band2["drums"] = "Dude"
# print(band)
band2 = band.copy()
band2["drums"] = "Dude"
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "Vocals"
    }
member2 = {
    "name": "Page",
    "instrument": "guitar"
    }
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# Sets
nums = {1,2,3,4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)

#no duplicates allowed
nums = {1,2,2,3}
print(nums)

# true is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)
# but you cannot refer to an element in a set with an index position or a key

# add a new element to a set
nums.add(8)
print (nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)
# you can use update with lists, tuples, and dictionaries too

# merge 2 sets to create a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# merge 2 sets keep only dupes
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# merge 2 sets keep non dupes
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)