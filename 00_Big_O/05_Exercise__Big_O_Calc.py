# What is the Big O of the below function? (Hint, you may want to go line by line)


def bigOCalc(input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(input)):  # O(n)
        anotherFunc()  # O(n) - (assuming anotherFunc is O(1))
        stranger = True  # O(n)
        a += 1  # O(n)

    return a  # O(1)


bigOCalc(input)

# 3 + n + n + n + n = 4n + 3
# Big O(4n + 3)

# Total running time of the bigOCalc function:
# O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(4n + 3)
#
# Big‑O rules:
# - Constant factors are removed: 4n → n
# - Constant terms are removed: + 3 disappears
# - n + constant → just n
#
# Final result: O(n)
