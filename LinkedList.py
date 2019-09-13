class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
        if node is None:
            print("Your singly linked list in empty. Please add some data to it.")
        while node is not None:
            print(node.data)
            node = node.next

    def insert_node_beginning(self, data):
        head_node = self.head
        if head_node is None:
            self.head = Node(data)
            return
        self.head = Node(data)
        self.head.next = head_node

    def insert_node_end(self, data):
        current_node = self.head
        if current_node is None:
            self.head = Node(data)
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    def insert_between_nodes(self, first_node_data, second_node_data, data):
        if first_node_data is None or second_node_data is None or data is None:
            print("None is not allowed.")
            return
        current_node = self.head
        while current_node.data != first_node_data:
            current_node = current_node.next
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def remove_node(self, removeNode):
        current_node = self.head
        if current_node is not None:
            if current_node.data == removeNode:
                self.head = current_node.next
                current_node = None
                return

        while current_node is not None:
            if current_node.data == removeNode:
                break
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print("Please pass a different value besides none.")
            return

        prev.next = current_node.next
        current_node = None

    def find_node(self, data):
        if data is None:
            print("Data value can not be None. Please pass a valid data value.")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                print("The value {0} is in the list.".format(data))
                break
            current_node = current_node.next

        if current_node is None:
            print("The value {0} is not present in the list.".format(data))


if __name__ == "__main__":

    # Create singly linked list
    single_linked_list = SLinkedList()
    single_linked_list.insert_node_beginning("Sunday")
    print("1. Initial list:")
    single_linked_list.display()

    # Insert Monday and Wednesday
    single_linked_list.insert_node_end("Monday")
    single_linked_list.insert_node_end("Wednesday")
    single_linked_list.insert_node_end("Thursday")
    single_linked_list.insert_node_end("Friday")
    single_linked_list.insert_node_end("Saturday")
    print("")
    print("2. List after inserting all the days of the week but Tuesday:")
    single_linked_list.display()

    # Insert Tuesday between Monday and Wednesday
    print("")
    print("3. List after inserting Tuesday between Monday and Wednesday")
    single_linked_list.insert_between_nodes("Monday", "Wednesday", "Tuesday")
    single_linked_list.display()

    # Remove Thursday
    print("")
    print("4. Removing Thursday from the list")
    single_linked_list.remove_node("Thursday")
    single_linked_list.display()

    # Look for Thursday after removing it
    print("")
    print("5. Looking for Thursday after removing it")
    single_linked_list.find_node("Thursday")
    single_linked_list.display()

    # # Look for Monday
    print("")
    print("6. Looking for Monday")
    single_linked_list.find_node("Monday")
    single_linked_list.display()
