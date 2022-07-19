class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None and q is None:
                return True

            if p is not None and q is None:
                return False

            if p is None and q is not None:
                return False

            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        q = [root]

        while q:
            size = len(q)
            while size > 0:
                cur_node = q.pop()
                size -= 1
                if isSameTree(cur_node, subRoot):
                    return True
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return False
