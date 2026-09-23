# O(n^2) - Quadratic Time

# Log all pairs of array


boxes = [1, 2, 3, 4, 5]


def logPairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"{arr[i]}:{arr[j]}")


logPairs(boxes)

# O(n^2)


def compressBox(input1, input2):
    for i in range(len(input1)):  # O(n)
        print(input1[i])

    for j in range(len(input2)):  # O(m)
        print(input2[j])


compressBox(input1, input2)

# O(n + m)
# O(n * m) - Nested loops with different inputs
