# Given a string, reverse it and return the result.
# For example, if the string is "Hi how are you?",
# the output should be "?uoy era woh iH".

# First Solution (Brute Force) - O(n) time complexity / O(n) space complexity

string = "Hello"


def reverseStr(string: str) -> str:
    newStr = []
    for i in range(len(string) - 1, -1, -1):
        newStr.append(string[i])
    return "".join(newStr)


print(reverseStr(string))  # Output: "olleH"

# Second Solution (Pointers)
# A smarter approach would be to take a pair of characters from opposite ends
# of the string and swap them.
# We would start at both ends and continue swapping pairs until we reach the middle.
# Best-case time: O(n) because the loop still runs
# Worst-case time: O(n²) because swap() creates and joins a full string each time
# Best-case space: O(1) additional space if no swaps occur
# Worst-case space: O(n) because swap() creates a list and string


def swap(string: str, a: int, b: int) -> str:
    newStr = list(string)
    temp = newStr[a]
    newStr[a] = newStr[b]
    newStr[b] = temp
    return "".join(newStr)


def smarter_reverse(string: str) -> str:
    newStr = string
    for idx in range(len(string) // 2):
        oppisite = len(string) - 1 - idx
        if string[idx] == string[oppisite]:
            continue  # Skip swapping if the characters are the same
        newStr = swap(newStr, idx, oppisite)
    return newStr


print(smarter_reverse(string))  # Output: "olleH"


# Apart from these, some built-in functions that can be used to reverse a string are as follows:

string1 = "abcde"
string2 = reversed(string1)
print("".join(string2))
# "".join(reversed(string1))

list1 = list(string1)
list1.reverse()
print("".join(list1))

# Both these methods are of O(n) time complexity
