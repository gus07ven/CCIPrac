
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
        print("")

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        new_node = Node(data)
        current_node.prev = new_node
        new_node.next = current_node
        self.head = new_node

    def insert_between(self, first_node_data, second_node_data, data):
        if first_node_data is None or second_node_data is None or data is None:
            print("None of the values can be null. Please use valid values.")
            return
        current_node = self.head
        first_node = None
        while current_node is not None:
            if current_node.data == first_node_data and current_node.next.data == second_node_data:
                first_node = current_node
                break
            current_node = current_node.next
        node_to_insert = Node(data)
        second_node = first_node.next
        node_to_insert.prev = first_node
        node_to_insert.next = second_node
        first_node.next = node_to_insert
        second_node.prev = node_to_insert

    def insert_at_end(self, data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        node_to_insert = Node(data)
        current_node.next = node_to_insert
        node_to_insert.prev = current_node
        node_to_insert.next = None


if __name__ == "__main__":

    # Create doubly linked list skipping Wednesday, and Saturday
    print("Creating days of the week without Wednesday and Saturday:")
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_beginning("Friday")
    doubly_linked_list.insert_at_beginning("Thursday")
    doubly_linked_list.insert_at_beginning("Tuesday")
    doubly_linked_list.insert_at_beginning("Monday")
    doubly_linked_list.insert_at_beginning("Sunday")
    doubly_linked_list.display()

    # Insert Wednesday between Tuesday and Thursday
    print("Inserting Wednesday between Tuesday and Thursday:")
    doubly_linked_list.insert_between("Tuesday", "Thursday", "Wednesday")
    doubly_linked_list.display()

    # Insert Saturday at end
    print("Inserting Saturday at end of doubly linked list")
    doubly_linked_list.insert_at_end("Saturday")
    doubly_linked_list.display()





