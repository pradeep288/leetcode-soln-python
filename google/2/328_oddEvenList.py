class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd, even = head, head.next
        oddh, evenh = head, head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            even.next = odd.next
            odd = odd.next
            even = even.next
        odd.next = evenh
        even.next = None

        return oddh
