# Space complexity O(1)
def boooo(n):
    for i in range(n):
        print("booooo")


# Space complexity O(n)
def arrayOfHiNTimes(n):
    hi_array = []
    for i in range(n):
        hi_array.append("hi")
    return hi_array


arrayOfHiNTimes(6)
