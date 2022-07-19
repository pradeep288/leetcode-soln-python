class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return cloned

        q = [cloned]

        while len(q) > 0:
            size = len(q)
            while size > 0:
                cur_node = q.pop(0)
                size -= 1
                if cur_node.val == target.val:
                    return cur_node

                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)

        return None
