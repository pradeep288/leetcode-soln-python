class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, cur_sum):
            if node is None:
                return 0

            cur_sum <<= 1
            cur_sum += node.val

            if node.left is None and node.right is None:
                return cur_sum

            return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)

        return dfs(root, 0)
