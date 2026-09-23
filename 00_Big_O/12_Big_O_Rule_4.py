# Rule 4 - Drop Non-dominant Terms
# When we have multiple terms in a Big O expression, we only keep the dominant term.


def printAllNumbersThenAllPairSums(numbers):
    print("these are the numbers:")
    for number in numbers:
        print(number)

    print("and these are their sums:")
    for firstNumber in numbers:
        for secondNumber in numbers:
            print(firstNumber + secondNumber)

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])

# O(n + n^2)
# O(n^2) - Drop Non-dominant Terms