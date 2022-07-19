class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        cur_sum = 0

        def reverse_inorder(node):
            nonlocal cur_sum
            if node is None:
                return 0

            right = reverse_inorder(node.right)
            cur_sum += node.val
            node.val = cur_sum
            reverse_inorder(node.left)

        reverse_inorder(root)

        return root
