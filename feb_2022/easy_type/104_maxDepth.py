from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 0
        q = Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            depth += 1
            while size != 0:
                cur_node = q.get()
                if cur_node.left is not None:
                    q.put(cur_node.left)
                if cur_node.right is not None:
                    q.put(cur_node.right)
                size -= 1

        return depth
'''


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if root is None:
                return depth

            depth += 1

            left_depth = dfs(root.left, depth)
            right_depth = dfs(root.right, depth)

            return max(left_depth, right_depth)

        return dfs(root, 0)
