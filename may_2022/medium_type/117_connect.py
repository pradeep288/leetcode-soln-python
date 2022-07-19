class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        nodes = [root]
        level_order = []

        while len(nodes) > 0:
            size = len(nodes)
            cur_level = []
            while size > 0:
                cur_node = nodes.pop(0)
                cur_level.append(cur_node)
                if cur_node.left:
                    nodes.append(cur_node.left)
                if cur_node.right:
                    nodes.append(cur_node.right)
                size -= 1
            level_order.append(cur_level)

        for cur_level in level_order:
            for i in range(len(cur_level) - 1):
                cur_level[i].next = cur_level[i + 1]
            cur_level[i].next = None

        return root
