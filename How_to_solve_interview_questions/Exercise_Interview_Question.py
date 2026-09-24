# Give 2 arrays. Create a function that let's a user know (true/false)
# Whether these two arrays contain any comon items

#  Example:
#  array1 = ["a", "b", "c", "x"]
#  array2 = ["z", "y", "i"]
#  should return false.

#  array1 = ["a", "b", "c", "x"]
#  array2 = ["z", "y", "x"]
#  should return true.

# 2 params - arrays - no size limit
# returns true/false

# Coule use nested loops to compare but is O(n^2) / O(n*m) - not efficient

arr1 = ["a", "b", "c", "x"]
arr2 = ["z", "y", "i"]


def containsCommonItems1(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


# arr1 ==> {"a": True, "b": True, "c": True, "x": True}
# arr2[i] == arr1.properties
# O(n) + O(m) => O(a + b) => O(n)


def containsCommonItems2(arr1, arr2):
    seen = {}

    for i in range(len(arr1)):
        item = arr1[i]
        if item not in seen:
            seen[item] = True

    for i in range(len(arr2)):
        item = arr2[i]
        if item in seen:
            return True

    return False


# def containsCommonItems2(arr1, arr2):
#     seen = {}
#
#     for item in arr1:
#         seen[item] = True
#
#     for item in arr2:
#         if item in seen:
#             return True
#
#     return False


print(containsCommonItems2(arr1, arr2))
