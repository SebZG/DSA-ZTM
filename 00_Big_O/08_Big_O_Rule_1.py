# Rule 1 - Worst Case
# When analyzing an algorithm, we always consider the worst case scenario.
# This is because we want to know the maximum time an algorithm can take to complete.

import time

everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

def find_nemo(array):
    t0 = time.perf_counter()
    for item in array:
        print("running")
        if item == "nemo":
            print("Found NEMO!")
            break
    t1 = time.perf_counter()
    print(f"Call to find Nemo took {(t1 - t0) * 1000:.4f} milliseconds.")


find_nemo(everyone)
