"""
You are given the pointer to the head node of a linked list and an integer to
add to the list. Create a new node with the given integer. Insert this node at
the tail of the linked list and return the head node of the linked list formed
after inserting this new node. The given head pointer may be null, meaning that
the initial list is empty.

Input Format
You have to complete the Node* Insert(Node* head, int data) method. It takes two
arguments: the head of the linked list and the integer to insert. You should not
read any input from the stdin/console.

Output Format
Insert the new node at the tail and just return the head of the updated linked
list. Do not print anything to stdout/console.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    curr = head
    if not curr:
        return Node(data)
    else:
        while curr:
            if curr.next:
                curr = curr.next
            else:
                curr.next = Node(data)
                return head
