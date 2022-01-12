class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[
        TreeNode]:

        if root is None:
            return TreeNode(val)

        cur_node = root
        while True:
            if cur_node.val > val:
                if cur_node.left is None:
                    cur_node.left = TreeNode(val)
                    return root
                cur_node = cur_node.left
            elif cur_node.val < val:
                if cur_node.right is None:
                    cur_node.right = TreeNode(val)
                    return root
                cur_node = cur_node.right
