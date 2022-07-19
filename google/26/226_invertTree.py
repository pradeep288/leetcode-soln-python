class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        q = [root]
        level_order = []
        while len(q) > 0:
            size = len(q)
            cur_level = []
            while size > 0:
                cur_node = q.pop()
                cur_level.append(cur_node)
                size -= 1
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            level_order.append(cur_level)

        while cur_level in level_order:
            s, e = 0, len(cur_level) - 1
            while s < e:
                cur_level[s].val, cur_level[e].val = cur_level[e].val, cur_level[s].val
                s += 1
                e -= 1

        return root
