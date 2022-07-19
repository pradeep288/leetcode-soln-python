# https://www.youtube.com/watch?v=bJBwOMPhe6Y
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []

        def traverse_inorder(node):
            if node is None:
                return

            traverse_inorder(node.left)
            temp.append(node)
            traverse_inorder(node.right)

        traverse_inorder(root)

        srt = sorted([n.val for n in temp])

        for i in range(len(srt)):
            temp[i].val = srt[i]

        return root
