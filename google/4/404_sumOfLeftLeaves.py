class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root
        q, res = [root], 0

        while len(q) > 0:
            size = len(q)
            while size > 0:
                cur = q.pop(0)
                size -= 1
                if cur.left:
                    q.append(cur.left)
                    if not cur.left.left and not cur.left.right:
                        res += cur.left.val
                if cur.right:
                    q.append(cur.right)

        return res
