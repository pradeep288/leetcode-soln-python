class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head, temp = None, None
        prev_node, cur_node, next_node = ListNode(val=-100, next=head), \
                                         head, \
                                         head.next

        while cur_node is not None and next_node is not None:
            if prev_node.val != cur_node.val and cur_node.val != next_node.val:
                new_node = ListNode(val=cur_node.val,next=None)
                if new_head is None:
                    new_head = new_node
                    temp = new_node
                else:
                    temp.next = new_node
                    temp = temp.next
            prev_node = prev_node.next
            cur_node = cur_node.next
            next_node = next_node.next

        if cur_node.val != prev_node.val:
            new_node = ListNode(val=cur_node.val,next=None)
            if new_head is None:
                return new_node
            else:
                temp.next = new_node

        return new_head
