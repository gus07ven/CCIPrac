
class Leet872:

    class TreeNode:

        def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None


if __name__ == "__main__":
    root = Leet872.TreeNode(5)
    root.left = Leet872.TreeNode(3)
    root.right = Leet872.TreeNode(6)
    root.left.left = Leet872.TreeNode(2)
    root.left.right = Leet872.TreeNode(4)

    root2 = Leet872.TreeNode(5)
    root2.left = Leet872.TreeNode(3)
    root2.right = Leet872.TreeNode(6)
    root2.left.left = Leet872.TreeNode(2)
    root2.left.right = Leet872.TreeNode(4)
    result = Leet872.increasing_BST(root)
