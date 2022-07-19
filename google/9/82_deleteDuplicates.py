class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy_node = ListNode(0, head)
        cur_node, prev_node = head, dummy_node

        while cur_node and cur_node.next:
            if cur_node.val != cur_node.next.val:
                prev_node.next = cur_node
            else:
                while cur_node.next and cur_node.val == cur_node.next.val:
                    cur_node = cur_node.next
                prev_node.next = cur_node.next
            cur_node = cur_node.next

        return dummy_node.next
