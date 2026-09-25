class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the linked list is empty, both head and tail point to the new node.
            self.head = new_node
            self.tail = new_node
        else:  # Else, we make the previous pointer of the new node point to the present tail.
            new_node.previous = self.tail
            # Connect the current tail to the new node, then update the tail.
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Point the new node to the current head.
            self.head.previous = (
                new_node  # Point the current head back to the new node.
            )
            self.head = new_node  # Update the head.
        self.length += 1

    def insert(self, position, data):
        if position < 0:
            print("Position must be non-negative.")
            return
        if position == 0:
            # Inserting at position 0 is equivalent to prepending, so reuse that method.
            self.prepend(data)
            return
        if position >= self.length:
            if position > self.length:
                print(
                    "This position is not available. Inserting at the end of the list."
                )
            # Inserting at a position greater than or equal to the length appends the node.
            self.append(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next
        new_node.previous = current_node
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.next.previous = new_node
        self.length += 1

    def delete_by_value(self, data):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        while current_node is not None and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            print("Given value not found.")
            return

        if current_node.previous is None:
            self.head = current_node.next
        else:
            current_node.previous.next = current_node.next

        if current_node.next is None:
            self.tail = current_node.previous
        else:
            current_node.next.previous = current_node.previous

        self.length -= 1

    def delete_by_position(self, position):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        if position < 0:
            print("Position must be non-negative.")
            return

        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.previous = None
            self.length -= 1
            return

        if position >= self.length:
            position = self.length - 1

        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next is not None:
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return


# Create a doubly linked list and call all its methods in the same sequence
# as in the singly linked list implementation. The results should be the same.
my_linked_list = DoublyLinkedList()
my_linked_list.print_list()
# Empty

my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.print_list()
# 5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list()
# 4 5 2 9

my_linked_list.insert(2, 7)
my_linked_list.print_list()
# 4 5 7 2 9

my_linked_list.insert(0, 0)
my_linked_list.insert(6, 0)
my_linked_list.insert(9, 3)
my_linked_list.print_list()
# This position is not available. Inserting at the end of the list
# 0 4 5 7 2 9 0 3

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
# 0 4 5 7 2 9 0

my_linked_list.delete_by_value(0)
my_linked_list.print_list()
# 4 5 7 2 9 0

my_linked_list.delete_by_position(3)
my_linked_list.print_list()
# 4 5 7 9 0

my_linked_list.delete_by_position(0)
my_linked_list.print_list()
# 5 7 9 0

my_linked_list.delete_by_position(8)
my_linked_list.print_list()
# 5 7 9

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
# Given value not found.

print(my_linked_list.length)
# 3


# The results are all the same, which means our doubly linked list works properly.
