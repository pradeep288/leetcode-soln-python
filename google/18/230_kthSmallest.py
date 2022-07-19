import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []

        def traverse_inorder(node):
            if node is None:
                return

            traverse_inorder(node.left)
            heapq.heappush(hp, node.val)
            traverse_inorder(node.right)

        traverse_inorder(root)

        return hp[k - 1]
