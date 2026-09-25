# The average time complexity of some operations invloving linked lists are as follows:
# Look-up : O(n)
# Insert : O(n)
# Delete : O(n)
# Append : O(1)
# Prepend : O(1)
# Python doesn't have a built-in implementation of linked lists, we have to build it on our own


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1

    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            currNode = self.head
            while currNode is not None:
                print(currNode.data, end=" ")
                currNode = currNode.next
            print()

    def insert(self, position, data):
        if position <= 0:
            self.prepend(data)
        elif position >= self.length:
            if position > self.length:
                print(
                    "This position is not available. Inserting at the end of the list"
                )
            self.append(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def delete_by_value(self, data):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is not None:
            current_node.next = current_node.next.next
            if current_node.next is None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")

    def delete_by_position(self, position):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return
        if position < 0:
            print("Position must be non-negative.")
            return
        if position >= self.length:
            position = self.length - 1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next is None:
            self.tail = current_node
        return


# We will import this file while reversing a linked list. So we must make sure that it runs only
# when it is the main file being run and not also when it is being imported in some other file.
if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.printList()
    # Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.printList()
    # 5 2 9

    my_linked_list.prepend(4)
    my_linked_list.printList()
    # 4 5 2 9

    my_linked_list.insert(2, 7)
    my_linked_list.printList()
    # 4 5 7 2 9

    my_linked_list.insert(0, 0)
    my_linked_list.insert(6, 0)
    my_linked_list.insert(9, 3)
    my_linked_list.printList()
    # This position is not available. Inserting at the end of the list
    # 0 4 5 7 2 9 0 3

    my_linked_list.delete_by_value(3)
    my_linked_list.printList()
    # 0 4 5 7 2 9 0

    my_linked_list.delete_by_value(0)
    my_linked_list.printList()
    # 4 5 7 2 9 0

    my_linked_list.delete_by_position(3)
    my_linked_list.printList()
    # 4 5 7 9 0

    my_linked_list.delete_by_position(0)
    my_linked_list.printList()
    # 5 7 9 0

    my_linked_list.delete_by_position(8)
    my_linked_list.printList()
    # 5 7 9

    print(my_linked_list.length)
    # 3