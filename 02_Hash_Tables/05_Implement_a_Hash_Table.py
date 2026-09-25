# Implementing a Hash Table in Python

# search - O(1)
# insert - O(1)
# lookup - O(1)
# delete - O(1)

# get - O(1)
# set - O(1)
# keys - O(n)
# values - O(n)

class Hash_Table():
    def __init__(self, size): # Initialize the hash table with a given size.
        self.size = size
        self.data = [None] * self.size

    def __str__(self):  # Customize the string representation of the hash table for easy printing.
        return str(self.__dict__)

    def _hash(self, key):  # Private method to compute the hash value for a given key.
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size  # Compute the hash using character codes and index.
        return hash

    def get(self, key):  # Retrieve the value associated with a given key in the hash table.
        hash = self._hash(key)
        if self.data[hash]:  # Multiple items may exist in the position of the hash value returned by the hash function, so we have to chceck all of them
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None  # Return None if the key is not found.

    def set(self, key, value):  # Insert a key-value pair into the hash table.
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] =  [[key, value]]
        else:
            self.data[hash].append([key, value])

    def keys(self): # Function to return all the keys
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
        values_arr = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_arr.append(self.data[i][j][1])
        return values_arr


new_hash = Hash_Table(2)
print(new_hash)
#{'size': 2, 'data': [None, None]}

new_hash.set('one',1)
new_hash.set('two',2)
new_hash.set('three',3)
new_hash.set('four',4)
new_hash.set('five',5)
print(new_hash)
#{'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

print(new_hash.get('one'))
#1

print(new_hash.keys())
#['one', 'five', 'two', 'three', 'four']
print(new_hash.values())
#[1, 5, 2, 3, 4]
