class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_vals = []

        def traverse_order(node):
            if node is None:
                return
            traverse_order(node.left)
            node_vals.append(node.val)
            traverse_order(node.right)

        traverse_order(root)

        return node_vals[k - 1]
