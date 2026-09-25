# Google Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6
# Example 3 : array = [2,1,4,5,6,3]
# It should return None

# First Solution (Brute Force)
# Loop the different permutations of the array and check if any element is repeated. If yes, return that element. If no, return None.
# Nested Loop - O(n²) time complexity / O(1) space complexity

array = [2, 1, 4, 2, 6, 5, 1, 4]


def bruteFRC(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return None


print(bruteFRC(array))

# Second Solution (Hash Table)
# Loop through the array and check if the element is already in the hash table.
# If yes return that element. If no, add it to the hash table.
# If no element is repeated, return None.
# O(n) time complexity / O(n) space complexity


def hashFRC(arr):
    seen = set()
    for val in arr:
        if val in seen:
            return val
        else:
            seen.add(val)
    return None
