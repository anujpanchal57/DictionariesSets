fruit = {"orange": "a sweet, orange coloured fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "Can I have some more fruit, please"}

print(veg)

# Adding fruit dictionary to the veg dictionary,
# It merges fruit dict into the veg dict
# veg.update(fruit)
# print(veg)

# # This line returns NONE
# print(fruit.update(veg))

# # This line returns the merged dicts of fruit and veg
# print(fruit)

# Merging two dicts with the help of COPY Method
CopyExample = fruit.copy()
CopyExample.update(veg)
print(CopyExample)