class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root

        level_order = []
        q = [(root, 0)]
        width = 1
        while len(q) > 0:
            size = len(q)
            cur_level = []
            while size > 0:
                cur_node, i = q.pop()
                cur_level.append(cur_node)
                if cur_node.left:
                    q.append((cur_node.left, i * 2))
                if cur_node.right:
                    q.append((cur_node.right, i * 2 + 1))

            _, start_idx = cur_level[0]
            _, end_idx = cur_level[-1]
            width = max(width, end_idx - start_idx + 1)

        return width
