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


if __name__ == "__main__":

    # Create nodes
    monday = Node("Monday")
    tuesday = Node("Tuesday")
    wednesday = Node("Wednesday")
    thursday = Node("Thursday")
    friday = Node("Friday")

    single_linked_list = SLinkedList()
    single_linked_list.head = monday
    monday.next = tuesday
    # tuesday.next = wednesday
    wednesday.next = thursday
    thursday.next = friday

    # single_linked_list.insert_node_beginning("Sunday")
    single_linked_list.insert_node_end("Saturday")
    single_linked_list.insert_between_nodes(monday, tuesday, "Wednesday")
    single_linked_list.display()
