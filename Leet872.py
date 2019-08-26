from typing import List


class Leet872:

    class TreeNode:

        def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None

    @staticmethod
    def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False

        leaves1 = Leet872.get_leaves(root1, [])
        leaves2 = Leet872.get_leaves(root2, [])

        if len(leaves1) != len(leaves2):
            return False
        else:
            return leaves1 == leaves2

    @staticmethod
    def get_leaves(root: TreeNode, leaves: List) -> List:
        if root is None:
            return None
        if root.left is not None:
            Leet872.get_leaves(root.left, leaves)
        if root.left is None and root.right is None:
            leaves.append(root.val)
        if root.right is not None:
            Leet872.get_leaves(root.right, leaves)
        return leaves


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
    print(Leet872.leaf_similar(root, root2))
