class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]

        level_order = []

        while q:
            size = len(q)
            cur_level = []
            while size > 0:
                cur_node = q.pop(0)
                size -= 1
                cur_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            level_order.append(cur_level)

        res = []
        for level in level_order:
            res.append(level[-1])

        return res
