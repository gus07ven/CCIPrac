from typing import List


class Leet429:

    class Node:
        def __init__(self, val, children):
            self.val = val
            self.children = children

    @staticmethod
    def level_order(root: Node) -> List[List[int]]:
        return get_level_order(root, [], 0)

    @staticmethod
    def get_level_order(root: Node, levels: List[List[int]], level: int) -> List[List[int]]:
        if root is None:
            return levels
        if level >= len(levels):
            levels.insert(level, [])

        levels[level].append(root.val)
        if root.children is not None:
            for child in root.children:
                Leet429.get_level_order(child, levels, level + 1)
        else:
            return levels
        return levels










