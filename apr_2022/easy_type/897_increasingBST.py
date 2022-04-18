class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def traverse_inorder(node):
            if not node:
                return

            traverse_inorder(node.left)
            arr.append(node.val)
            traverse_inorder(node.right)

        # Get the values of nodes in increasing order by Inorder traversal
        traverse_inorder(root)

        # Recreate the BST using the values obtained in the earlier step
        head = TreeNode()
        cur_node = head
        for i in range(len(arr)):
            new_node = TreeNode(val=arr[i])
            cur_node.right = new_node
            cur_node = new_node

        return head.right
