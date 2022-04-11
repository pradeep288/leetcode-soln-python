class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[
        ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        # Get the count of Nodes and last node
        cur_node, count, prev_node = head, 0, None
        while cur_node is not None:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        last_node = prev_node

        split_index = count - (k % count) if k > count else count - k

        if split_index > 0:
            i = 1
            cur_node = head
            while i < split_index:
                cur_node = cur_node.next
                i += 1
            last_node.next = head
            head = cur_node.next
            cur_node.next = None

        return head