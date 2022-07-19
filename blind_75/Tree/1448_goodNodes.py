class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, cur_max):
            if node is None:
                return
            nonlocal res
            if node.val >= cur_max:
                res += 1
            cur_max = max(cur_max, node.val)

            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        dfs(root, float('-inf'))

        return res
