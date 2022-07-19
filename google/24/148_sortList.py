import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hp = []  # (val, node)
        cur = head
        while cur:
            heapq.heappush(hp, (cur.val, cur))
            cur = cur.next

        dummy_node = ListNode(val=-1000)
        cur = dummy_node

        while hp:
            _, node = heapq.heappop(hp)
            cur.next = node
            cur = node

        return dummy_node.next
