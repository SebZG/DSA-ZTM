# Implement our own array with common methods such as get, push, pop, insert, and delete.

# search - O(n) - Linear Time
# insert - O(n) - Linear Time
# push* - O(1) - Constant Time
# lookup - O(1) - Constant Time
# delete - O(n) - Linear Time

# get - O(1) - Constant Time
# push* - O(1) - Constant Time
# pop - O(1) - Constant Time
# insert - O(n) - Linear Time
# delete - O(n) - Linear Time

from typing import Any


class MyArray:
    def __init__(self):
        self.length = 0  # Initialize the array's length to zero.
        self.data = {}  # Use a dictionary to store the array's elements. The keys are the element indices, and the values are the elements themselves.

    # By default, the class's attributes are stored in a dictionary.
    # Calling __dict__ on an instance returns its attributes and their values as a dictionary.
    # Without a custom __str__ method, printing an instance displays the class name and its memory address.
    # We want printing the array to display its elements instead.
    # Therefore, we customize the class's __str__ method.

    def __str__(self):
        # Print the array's attributes as a string when print(array_instance) is called.
        return str(self.__dict__)

    def get(self, index: int) -> Any:
        return self.data[index]  # Return the element at the specified index in O(1) time.

    def push(self, item: Any) -> None:
        self.length += 1
        self.data[self.length - 1] = item  # Add an item to the end of the array in O(1) time.

    def pop(self) -> Any:
        last_item = self.data[self.length - 1]  # Get the last item in the array.
        del self.data[self.length - 1]  # Delete the last item in the array.
        self.length -= 1  # Decrease the array's length by one.
        return last_item  # Return the last item in O(1) time.

    def insert(self, index: int, item: Any) -> None:
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]  # Shift elements one position to the right to make room for the new item. O(n) time.
        self.data[index] = item  # Insert the new item at the specified index.

    def delete(self, index: int) -> None:
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # Shift elements one position to the left. O(n) time.
        del self.data[self.length - 1]  # Delete the last item in the array.
        self.length -= 1  # Decrease the array's length by one.


arr = MyArray()
arr.push(6)
#{'length': 1, 'data': {0: 6}}

arr.push(2)
# {'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
# {'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
# {'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
# {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3, 10)
# {'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)
# {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))
# 2

print(arr)

# The dictionary states shown above are expected results after each operation.
# They appear only when the array is explicitly printed with print(arr).
