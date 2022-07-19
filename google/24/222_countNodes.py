class TreeNode:
    def _init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_left_height(self, node):
        count = 0

        while node:
            node = node.left
            count += 1

        return count

    def find_right_height(self, node):
        count = 0

        while node:
            node = node.right
            count += 1

        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        lh = self.find_left_height(root)
        rh = self.find_right_height(root)

        if lh == rh:
            return (2 ** lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
