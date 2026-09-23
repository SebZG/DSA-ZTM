# O(1) — Constant Time Complexity
# Number of operations does NOT grow with input size:
# it stays fixed, regardless of how large the array is.

import time

array_small = ["nemo" for _ in range(10)]
array_medium = ["nemo" for _ in range(100)]
array_large = ["nemo" for _ in range(100_000)]


def finding_nemo(array):
    t0 = time.perf_counter()
    print(array[0])  # O(1) — direct index lookup
    print(array[1])  # O(1) — fixed, same work always
    t1 = time.perf_counter()
    print(f"Time taken = {t1 - t0:.8f} seconds\n")


finding_nemo(array_small)  # ~same time
finding_nemo(array_medium)  # ~same time
finding_nemo(array_large)  # ~same time

# Why O(1) and not O(2)?
# Big‑O ignores constant values — O(2), O(100), O(5000)
# all mean the same: work is fixed and does not scale with n.
