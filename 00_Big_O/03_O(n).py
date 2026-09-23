# O(n) - Linear Time
# The number of operations grows linearly with the size of the input.

import time

nemo = ["nemo"]
everyone = [
    "dory",
    "bruce",
    "marlin",
    "nemo",
    "gill",
    "bloat",
    "nigel",
    "squirt",
    "darla",
]
large = ["nemo" for i in range(100000)]


def find_nemo(array):
    t0 = time.perf_counter()
    for i in range(0, len(array)):
        if array[i] == "nemo":
            print("Found Nemo!!")
    t1 = time.perf_counter()
    print(f"The search took {t1 - t0} seconds.")


find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)


def funchallenge(input):
    temp = 10  # O(1)
    temp = temp + 50  # O(1)
    for i in range(len(input)):  # O(n)
        var = True  # n*O(1)
        a += 1  # n*O(1)
    return a  # O(1)


funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)


# Total running time of the funchallenge function:
# O(1 + 1 + n + n*1 + n*1 + 1) = O(3n + 3)
#
# Big‑O rules:
# - Constant factors are removed: 3n → n
# - Constant terms are removed: + 3 disappears
# - n + constant → just n
#
# Final result: O(n)
