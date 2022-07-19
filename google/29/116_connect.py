class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        q = [root]
        level_order = []
        while len(q) > 0:
            size = len(q)
            cur_level = []
            while size > 0:
                size -= 1
                cur_node = q.pop(0)
                cur_level.append(cur_node)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            level_order.append(cur_level)

        for cur_level in level_order:
            for i in range(len(cur_level)-1):
                cur_level[i].next = cur_level[i + 1]
            cur_level[len(cur_level) - 1].next = None

        return root
