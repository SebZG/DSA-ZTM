# Rule 2 - Remove Constants
# When we have a constant factor in our Big O notation, we can remove it.
# For example, if an algorithm takes 2n steps, we can simplify it to O(n).


def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])  # O(1)

    middle_index = len(items) // 2  # O(1) - integer division = Math.floor
    index = 0  # O(1)

    while index < middle_index:  # runs n/2 times
        print(items[index])  # O(n/2)
        index += 1  # O(n/2)

    for _ in range(100):  # always exactly 100 iterations
        print("hi")  # O(100)


# O(1 + 1 + 1 + n/2 + n/2 + 100) = O(n + 103)
# # Since we are dropping constants, the final Big O notation is O(n).