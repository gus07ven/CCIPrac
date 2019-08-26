
class Leet897:

    class TreeNode:

        def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None

    result = None
    head = None

    @staticmethod
    def increasing_BST(root: TreeNode) -> TreeNode:
        if root is None:
            return root
        if root.left is not None:
            Leet897.increasing_BST(root.left)

        if Leet897.result is None:
            Leet897.result = Leet897.TreeNode(root.val)
            Leet897.head = Leet897.result
        else:
            Leet897.result.left = None
            Leet897.result.right = Leet897.TreeNode(root.val)
            Leet897.result = Leet897.result.right

        if root.right is not None:
            Leet897.increasing_BST(root.right)

        return Leet897.head


if __name__ == "__main__":
    root = Leet897.TreeNode(5)
    root.left = Leet897.TreeNode(3)
    root.right = Leet897.TreeNode(6)
    root.left.left = Leet897.TreeNode(2)
    root.left.right = Leet897.TreeNode(4)
    result = Leet897.increasing_BST(root)

    while result is not None:
        print(result.val)
        result = result.right
