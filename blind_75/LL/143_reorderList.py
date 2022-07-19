from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        q = deque()
        while cur:
            q.append(cur)
            cur = cur.next

        dummy_node = ListNode(-100)
        prev_node = dummy_node

        while len(q) >= 2:
            odd_node = q.popleft()
            prev_node.next = odd_node
            even_node = q.pop()
            odd_node.next = even_node
            even_node.next = None
            prev_node = even_node

        if q:
            last_node = q.pop()
            prev_node.next = last_node
            last_node.next = None

        return dummy_node.next
