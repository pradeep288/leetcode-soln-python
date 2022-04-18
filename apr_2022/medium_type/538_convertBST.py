class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def traverse_inorder(node):
            if not node:
                return

            traverse_inorder(node.left)
            vals.append(node.val)
            traverse_inorder(node.right)

        # Get the values of nodes in increasing order by Inorder traversal
        traverse_inorder(root)

        greater_values = {}
        # create a hashmap
        for k, v in enumerate(vals):
            greater_values[v] = sum(vals[k:])

        # traverse tree and replace values with the obtained values
        def dfs(node):
            if not node:
                return
            node.val = greater_values[node.val]
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root
