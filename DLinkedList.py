
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        new_node = Node(data)
        current_node.next = new_node
        new_node.prev = current_node


if __name__ == "__main__":

    # Create doubly linked list and insert node at beginning
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_beginning("Monday")
    doubly_linked_list.insert_at_beginning("Tuesday")
    doubly_linked_list.display()




