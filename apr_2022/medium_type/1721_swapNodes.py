class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the length of the list
        cur_node = head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next

        # Point to the node, present at kth location
        cur_node, idx = head, 1
        while idx < k:
            idx += 1
            cur_node = cur_node.next
        node1 = cur_node

        # Point to the node, present at len(list)-k th location
        cur_node, idx = head, 1
        while idx < count - k+1:
            idx += 1
            cur_node = cur_node.next
        node2 = cur_node

        # swap node values
        node1.val, node2.val = node2.val, node1.val

        return head
