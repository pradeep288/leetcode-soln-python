class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    class Solution:
        def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
            def bfs(node):
                res = []

                if node is None:
                    res.append([0])
                    return res

                nodes = [node]
                level_order = []

                while len(nodes) > 0:
                    size = len(nodes)
                    cur_level = []
                    while size > 0:
                        cur_node = nodes.pop(0)
                        size -= 1
                        cur_level.append(cur_node.val)
                        if cur_node.left:
                            nodes.append(cur_node.left)
                        if cur_node.right:
                            nodes.append(cur_node.right)
                    level_order.append(cur_level)

                return level_order

            if root.left is None and root.right is None:
                return root.val

            left = bfs(root.left)
            right = bfs(root.right)

            if len(right) > len(left):
                return sum(right[-1])
            elif len(left) > len(right):
                return sum(left[-1])

            return sum(left[-1]) + sum(right[-1])
