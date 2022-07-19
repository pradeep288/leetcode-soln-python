class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0, True
            l_height, l_balanced = dfs(node.left)
            r_height, r_balanced = dfs(node.right)

            return max(l_height, r_height)+1, l_balanced and r_balanced and abs(l_height - r_height) <= 1

        return dfs(root)[1]