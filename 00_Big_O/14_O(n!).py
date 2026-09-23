# O(n!) - Factorial Time
# This is the slowest time complexity and is often seen in algorithms that generate all possible permutations of a set.
# For example, the number of permutations of n distinct objects is n!.


def factorial(n):
    for i in range(1, n + 1):  # O(n!)
        factorial(n - 1)  # O(n!)


factorial(10)  # O(n!) - Factorial Time
