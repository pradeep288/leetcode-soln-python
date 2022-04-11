class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur_node, next_node = head, head.next
        while True:
            cur_node.val, next_node.val = next_node.val, cur_node.val

            if next_node.next is None or next_node.next.next is None:
                break

            cur_node = next_node.next
            next_node = next_node.next.next

        return head
