# Declaring a set called farm_animals
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("- " * 40)

# This line shows an error because we haven't declared it as a literal
# wild_animals = set(["lion", "tiger", "panther", "elephant"])

# This will be right declaration
wild_animals = {"lion", "tiger", "panther", "elephant"}
print(wild_animals)

for animal in wild_animals:
    print(animal)

# Adds HORSE in farm_animals and wild_animals
farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

# This is an EMPTY SET
empty_set = set()

# This will give an error because it defines an EMPTY DICT and not an EMPTY SET
empty_set_2 = {}

empty_set.add("a")

# This will also give us an error because a DICT doesn't have ADD method
# empty_set_2.add("a")

even = set(range(0, 40, 2))
print(even)

# Declares a tuple by the name of squares
squares_tuple = (4, 6, 9, 16, 25)

# Converts SQUARES_TUPLE into a set SQUARES
squares = set(squares_tuple)
print(squares)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# Prints the Union Set of EVEN and SQUARES
print(even.union(squares))

# Prints out the length of the EVEN.UNION(SQUARES)
print(len(even.union(squares)))

# If we do SQUARES.UNION(EVEN), we'll get exactly the same output as above
print(squares.union(even))

print("- " * 40)

# It prints the intersection of two sets EVEN and SQUARES
print(even.intersection(squares))

# This line also prints the intersection of two sets EVEN and SQUARES
print(even & squares)

# These lines also print the same results as that of the above lines
print(squares.intersection(even))
print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

# This will print the result of difference between even and squares
print("EVEN MINUS SQUARES")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

# This will print the result of difference between squares and even
print("SQUARES MINUS EVEN")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

# This line updates the EVEN set after calculating the difference between the two sets
even.difference_update(squares)
print(sorted(even))

even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("\n")

# This will print the Symmetric difference between the two sets EVEN and SQUARES
print("Symmetric Difference Even minus Squares")
print(sorted(even.symmetric_difference(squares)))

print("\n")

# This will print the Symmetric Difference between the two sets SQUARES and EVEN
# Both will produce exactly the same results
print("Symmetric Difference Squares minus Even")
print(sorted(squares.symmetric_difference(even)))


# Discards the value 4 from the set
squares.discard(4)

# this also does the same thing as above, removes 16 from the set
squares.remove(16)

# No error, basically it does nothing
squares.discard(8)

print(squares)

# This will give us an error
# Inorder to solve this error, we can do this
if 8 in squares:
    squares.remove(8)

even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares))

print("\n")

# Checking whether it is a subset of EVEN or not
if squares.issubset(even):
    print("Squares is a subset of Even")

# Checking whether it is a superset of SQUARES or not
if even.issuperset(squares):
    print("Even is a superset of Squares")

# FROZEN SETS cannot be modified, means we cannot add, remove or update any contents of the FROZEN SETS
even = frozenset(range(0, 100, 2))
print(even)

# This will show us an error because FROZEN SETS have no attribute as ADD
even.add(3)


