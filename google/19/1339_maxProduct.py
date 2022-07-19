class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(node):
            if node is None:
                return 0
            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            sums.append(subtree_sum)
            return subtree_sum

        res = 0
        total = dfs(root)
        for i in sums:
            prod = i * (total - i)
            res = max(res, prod)

        return res % (10 ** 9 + 7)
