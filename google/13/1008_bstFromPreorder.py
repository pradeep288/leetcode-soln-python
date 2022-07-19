class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def add_node(cur, val):
            dummy_node = TreeNode(0)
            while cur:
                dummy_node = cur
                if cur.val > val:
                    cur = cur.left
                else:
                    cur = cur.right
            new_node = TreeNode(val)
            if dummy_node.val > val:
                dummy_node.left = new_node
            else:
                dummy_node.right = new_node

        for i in range(1, len(preorder)):
            add_node(root, preorder[i])

        return root
