class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if root is None:
            root = new_node
            return root

        cur = root
        prev = TreeNode(val)
        while cur:
            dummy = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        print(dummy.val)
        if dummy.val > val:
            dummy.left = new_node
        else:
            dummy.right = new_node
        return root
