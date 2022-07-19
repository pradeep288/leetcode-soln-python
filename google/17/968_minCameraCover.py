class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minCameraCover(self, root):
        cam = 0
        covered = set()
        covered.add(None)

        def dfs(node, parent):
            nonlocal cam
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if parent is None and not (node in covered) and not (node.left in covered) and not(node.right in covered):
                    cam+=1
                    covered.add(node)
                    covered.add(parent)
                    covered.add(node.left)
                    covered.add(node.right)
        if root is None:
            return 0
        dfs(root, None)

        return cam
