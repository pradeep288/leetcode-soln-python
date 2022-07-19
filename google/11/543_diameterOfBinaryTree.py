class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_diameter = max(max_diameter, left + right + 1)

            return max(left, right)+1
        dfs(root)

        return max_diameter-1
