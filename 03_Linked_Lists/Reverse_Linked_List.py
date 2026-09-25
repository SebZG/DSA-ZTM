# Given a linked list, reverse its nodes.
# The linked-list implementation is imported so we do not have to define the
# LinkedList and Node classes again in this file.

from Implementing_Linked_List import LinkedList

# Create a linked list by appending several values.
my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.printList()
# 2 3 4 5 6


# Reverse the links in the list in place.
# The first node becomes the tail, and the last node becomes the head.
# Time complexity: O(n). Space complexity: O(1).
def reverse(linked_list):
    if linked_list.length <= 1:
        return linked_list

    previous_node = None
    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    linked_list.head = previous_node
    return linked_list


reversed_linked_list = reverse(my_linked_list)
reversed_linked_list.printList()
# 6 5 4 3 2
