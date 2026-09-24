# Given two SORTED arrays, merge them into a single SORTED array.

array1 = ["a", "b", "c", "d"]
array2 = ["b", "d", "h"]

# First solution: merge the arrays, then sort the result.
# Time complexity: O((n + m) log(n + m))
# Space complexity: O(n + m)


def mergeAndSortArrays(arr1, arr2):
    # First, merge the two arrays into a single array.
    newArr = []
    for item in arr1:
        newArr.append(item)

    for item in arr2:
        newArr.append(item)

    # Then, sort the merged array.
    newArr.sort()

    return newArr


print(mergeAndSortArrays(array1, array2))

# The pointer-based solution requires both input arrays to already be sorted.
# Second solution: merge the arrays in sorted order using two pointers.
# Time complexity: O(n + m)
# Space complexity: O(n + m)


def sortAndMergeArrays(arr1, arr2):
    # Create a new array to hold the merged and sorted elements.
    newArr = []
    i = 0  # Pointer for arr1.
    j = 0  # Pointer for arr2.

    # While both arrays still contain unprocessed elements:
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newArr.append(arr1[i])
            i += 1
        else:
            newArr.append(arr2[j])
            j += 1

    # Add any remaining elements from arr1.
    while i < len(arr1):
        newArr.append(arr1[i])
        i += 1

    # Add any remaining elements from arr2.
    while j < len(arr2):
        newArr.append(arr2[j])
        j += 1

    return newArr


print(sortAndMergeArrays(array1, array2))


# Combine arrays and then sort the time complexity is:
# O((n + m) log(n + m)) where n is the length of arr1 and m is the length of arr2.

# Sorting the arrys first and then merging them with pointers is more efficient:

# Sorting arr1: O(n log n)
# Sorting arr2: O(m log m)
# Merging with pointers: O(n + m)
# Total time complexity: O(n log n + m log m)
# The merged result requires space for n + m elements: O(n + m)
# So the overall time complexity is O(n log n + m log m) and space complexity is O(n + m).