class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2 = [], []

        def traverse_inorder(node):
            if node is None:
                return
            traverse_inorder(node.left)
            l1.append(node.val)
            traverse_inorder(node.right)

        traverse_inorder(root1)
        traverse_inorder(root2)

        i, j = 0, 0
        res = []
        while i > len(l1)-1 and j > len(l1)-1:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l1[j])
                j += 1

        if i<len(l1)-1:
            res.append(l1[i:])
        elif j>len(l1)-1:
            res.append(l2[j:])

        return res

