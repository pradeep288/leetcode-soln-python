class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        nodes = []

        def preorder(node):
            if node is None:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        head = None
        for i in range(len(nodes)):
            if nodes[i].val < low or nodes[i].val > high:
                continue

            new_node = TreeNode(val=nodes[i].val)
            if head is None:
                head = new_node
            else:
                prev_node, cur_node = None, head
                while cur_node:
                    prev_node = cur_node
                    if nodes[i].val > cur_node.val:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left

                if prev_node.val > nodes[i].val:
                    prev_node.left = new_node
                else:
                    prev_node.right = new_node

        return head
