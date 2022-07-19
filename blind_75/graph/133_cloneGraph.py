class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# 1. Create Node
# 2. Associate Node
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        first_val = node.val
        old_to_new = {
            first_val: Node(first_val, [])
        }

        q = [node]
        while q:
            cur_node = q.pop(0)
            cloned_node = old_to_new[cur_node.val]
            for n in cur_node.neighbors:
                if n.val not in old_to_new:
                    old_to_new[n.val] = Node(n.val, [])
                    q.append(n)
                cloned_node.neighbors.append(old_to_new[n.val])
        return old_to_new[first_val]
