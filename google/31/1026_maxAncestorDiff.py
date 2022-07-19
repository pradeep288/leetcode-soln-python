class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = float('-inf')

        def find_subtree_max_diff(node):
            subtree_max_diff = float('-inf')
            q = [node]

            while len(q):
                size = len(q)
                while size > 0:
                    cur_node = q.pop(0)
                    size -= 1
                    subtree_max_diff = max(subtree_max_diff, abs(cur_node.val - node.val))
                    if cur_node.left:
                        q.append(cur_node.left)
                    if cur_node.right:
                        q.append(cur_node.right)
            return subtree_max_diff

        if root is None:
            return root

        q = [root]
        res = []
        while len(q):
            size = len(q)
            while size > 0:
                cur_node = q.pop(0)
                size -= 1
                val = find_subtree_max_diff(cur_node)
                res.append({cur_node.val: val})
                max_diff = max(max_diff, find_subtree_max_diff(cur_node))
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        print(res)

        return max_diff
