
class Leet559:

    class Node:
        def __init__(self, val, children):
            self.val = val
            self.children = children

    def max_depth(self, root: 'Node') -> int:
        if root is None:
            return 0

        max = 0
        for i in range(0, len(root.children)):
            getMax = self.max_depth(root.children[i])
            if getMax > max:
                max = getMax
        return max + 1
