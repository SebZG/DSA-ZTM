# Rule 3 - Different terms for inputs
# When we have different inputs to an algorithm, we need to consider each input separately.
# For example, if we have two arrays of different sizes, we cannot simply say O(n + m).
# We need to consider the size of each array individually.


def compressBox(input1, input2):
    for i in range(len(input1)):  # O(n)
        print(input1[i])

    for j in range(len(input2)):  # O(m)
        print(input2[j])


compressBox(input1, input2)

# O(n + m)


def compressBox2(input1, input2):
    for i in range(len(input1)):  # O(n)
        for j in range(len(input2)):  # O(m)
            print(f"{input1[i]}:{input2[j]}")


compressBox2(input1, input2)

# O(n * m) - Nested loops with different inputs
