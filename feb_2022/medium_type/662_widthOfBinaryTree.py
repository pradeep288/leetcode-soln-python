class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = [(root, 0)]

        max_width = float('-inf')

        while len(q) != 0:
            max_width = max(max_width, q[-1][1] - q[0][1]+1)
            size = len(q)
            while size > 0:
                cur_node, position = q.pop(0)
                size -= 1
                if cur_node.left != None:
                    q.append((cur_node.left, position * 2))
                if cur_node.right != None:
                    q.append((cur_node.right, position * 2 + 1))

        return max_width
