class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        total = 0

        def dfs(node, cur_sum):
            nonlocal total
            if node is None:
                return

            if cur_sum + node.val == targetSum:
                total += 1

            dfs(node.left, cur_sum + node.val)
            dfs(node.right, cur_sum + node.val)

        def helper(node):
            if node is None:
                return

            dfs(node, 0)
            helper(node.left)
            helper(node.right)

        helper(root)

        return total
