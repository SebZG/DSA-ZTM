# Hash tables are data structures that generally provide very fast (O(1)) lookups, insertions, and deletions.
# In Python, dictionaries are implemented as hash tables.

# Hashing works by using a bucket containing slots in which elements can be stored.
# As in arrays, elements are referenced by their integer indexes. In dictionaries, or hash tables,
# values are referenced by their keys, which can be of any data type.
# There are different kinds of hash functions (e.g., MD5, SHA-1, and SHA-256) that are used to
# convert keys into hashes. These hashes are then mapped to slots in the bucket.
# The key-value pair is stored in the slot or in an accompanying data structure within the slot
# (such as a linked list).

# In general, lookup, insertion, and deletion operations are all very fast, on the order of O(1).
# However, in some cases, more than one key can map to the same slot, which increases the time complexity
# by some amount, although usually not by much. This is known as a collision.
# As with almost all problems in computer science, there are solutions to collisions.
# They can be resolved using various collision-resolution techniques, such as open addressing
# and separate chaining.

# Enough detail; let's look at how hash tables are implemented in Python using dictionaries.

dictionary = dict()
dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(dictionary)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

print(dictionary.keys())
# dict_keys(['one', 'two', 'three', 'four', 'five'])

print(dictionary.values())
# dict_values([1, 2, 3, 4, 5])

print(dictionary.items())
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)])

print(dictionary["one"])  # Accessing a value by its key in O(1) time
# 1

dictionary["six"] = 6  # Inserting the value 6 for the key 'six' in O(1) time.
print(dictionary)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
