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


# Create nodes
sunday = Node("Sunday")
monday = Node("Monday")
tuesday = Node("Tuesday")
wednesday = Node("Wednesday")
thursday = Node("Thursday")
friday = Node("Friday")
saturday = Node("Saturday")


single_linked_list = SLinkedList()
single_linked_list.head = sunday
single_linked_list.head.next = monday
monday.next = tuesday
tuesday.next = wednesday
wednesday.next = thursday
thursday.next = friday
friday.next = saturday

single_linked_list.display()