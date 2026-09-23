# What is the Big O of the below function? (Hint, you may want to go line by line)


def anotherFunChallenge(input_n):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in range(input_n):  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(input_n):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoAmI = "I don't know"  # O(1)


# 4 + 4n + 3n
# Big O(7n + 4)
# O(n)