
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res

    def search(self, root, data):
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        if root.data > data:
            return self.search(root.left, data)


if __name__ == "__main__":

    root = Node(7)
    root.insert(16)
    root.insert(3)
    root.insert(14)
    # root.insert(5)
    # root.insert(2)
    # root.insert(18)
    # root.insert(23)
    # root.insert(24)

    print("The root of the tree is: {}".format(root.data))
    print("")

    print("Print tree:")
    root.print_tree()
    print("")

    print("In-order traversal of tree:")
    print(root.in_order_traversal(root))
    print("")

    print("Pre-order traversal of tree:")
    print(root.pre_order_traversal(root))
    print("")

    print("Post-order traversal of tree:")
    print(root.post_order_traversal(root))
    print("")

    print("Search for number 14:")
    result = root.search(root, 14)
    print(result.data)
    print("")





