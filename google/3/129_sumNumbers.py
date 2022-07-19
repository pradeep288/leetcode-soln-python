class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l = []

        def dfs(node, num):
            if node is None:
                return

            num = num * 10 + node.val
            if node.left is None and node.right is None:
                l.append(num)

            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)

        return sum(l)
