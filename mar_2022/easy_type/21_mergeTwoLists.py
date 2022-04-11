import heapq as hq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        heap = []

        while l1 is not None and l1 is not None:
            heap.append((l1.val, l1))
            heap.append((l2.val, l2))
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            heap.append((l1.val, l1))
            l1 = l1.next

        while l2 is not None:
            heap.append((l2.val, l2))
            l2 = l2.next

        hq.heapify(heap)
        _, head = hq.heappop(heap)
        temp = head
        while len(heap) > 0:
            _, node = hq.heappop(head)
            temp.next = node
            temp = node

        temp.next = None

        return head
