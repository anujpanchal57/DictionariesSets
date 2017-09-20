fruit = {"orange": "a sweet, orange coloured fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
         # "apple": "round and crunchy"} # This second apple overwrote the above
        # apple also to "round and crunchy"

# Prints out the fruit
print(fruit)

# Prints out details of lemon
print(fruit["lemon"])

# Adding an entry into the dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit)

# We're overwriting the entry in place of "an odd shaped apple" we'll get
# "great with tequila"
fruit["pear"] = "great with tequila"
print(fruit)

# Probably being more realistic, Lime goes great with tequila
fruit["lime"] = "great with tequila"
print(fruit)

# Deleting any key value
del fruit["lemon"]
print(fruit)

# Deleting the entire dictionary
del fruit

# Instead of above line, we can use the following, this will display an empty dictionary
fruit.clear()
# This will give us an error, because the entire dictionary no longer exists
print(fruit)

# If we try to enter a Key which is not present in the dictionary, we'll get an error
print(fruit["tomato"])

print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    # description = fruit.get(dict_key, "We don't have a " + dict_key)
    # print(description)
    # GET Method retrieves the value for a specified key from the dictionary
    # It doesn't give us an error if the Key doesn't exists, instead it prints out "NONE"
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)

# This will print each item in the fruit dictionary for 10 times
for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("-" * 40)

# If we want the dictionary to be printed out in an ordered manner
ordered_keys = list(fruit.keys())
ordered_keys.sort()
# This will do the same thing as above, but takes only a single line and uses the method SORTED
ordered_keys = sorted(list(fruit.keys()))

for f in ordered_keys:
    print(f + " - " + fruit[f])

# More shorter way of doing the same thing done above
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# Not an efficient method and should not be used
for val in fruit.values():
    print(val)

print("-" * 40)

# This one is the most efficient method to be used
for key in fruit:
    print(fruit[key])

# Prints the keys
print(fruit.keys())

# Prints the values
print(fruit.values())

# Printing out the keys in dictionary
fruit_keys = fruit.keys()
print(fruit_keys)

# Adding a key and value pair in the dict
fruit["tomato"] = "not good with ice cream"
print(fruit_keys)

# Prints out all the items in the dict including keys and values
print(fruit.items())

# For printing out a regular tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# Prints a regular Dict
print(dict(f_tuple))


