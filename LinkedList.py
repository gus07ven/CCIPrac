class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
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

    def insert_between_nodes(self, first_node, second_node, data):
        if first_node is None:
            print("First node can't be none.")
        new_node = Node(data)
        first_node.next = new_node
        new_node.next = second_node

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

    # Create nodes
    monday = Node("Monday")
    tuesday = Node("Tuesday")
    wednesday = Node("Wednesday")
    thursday = Node("Thursday")
    friday = Node("Friday")

    # Create incomplete list to test
    single_linked_list = SLinkedList()
    single_linked_list.head = monday
    monday.next = wednesday
    wednesday.next = thursday
    thursday.next = friday
    print("1. Initial list:")
    single_linked_list.display()

    # Insert Sunday at beginning of list
    single_linked_list.insert_node_beginning("Sunday")
    print("")
    print("2. List after inserting Sunday at beginning:")
    single_linked_list.display()

    # Insert Saturday at end of list
    single_linked_list.insert_node_end("Saturday")
    print("")
    print("3. List after inserting Saturday at end:")
    single_linked_list.display()

    # Insert Wednesday between
    print("")
    print("4. List after inserting Tuesday between Monday and Wednesday")
    single_linked_list.insert_between_nodes(monday, wednesday, "Tuesday")
    single_linked_list.display()

    # Remove Thursday
    print("")
    print("5. Removing Thursday from the list")
    single_linked_list.remove_node("Thursday")
    single_linked_list.display()

    # Look for Thursday after removing it
    print("")
    print("6. Looking for Thursday after removing it")
    single_linked_list.find_node("Thursday")
    single_linked_list.display()

    # Look for Thursday after removing it
    print("")
    print("7. Looking for Friday")
    single_linked_list.find_node("Friday")
    single_linked_list.display()