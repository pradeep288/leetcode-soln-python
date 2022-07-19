import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return lists
        hp = []

        def my_lt(self, other):
            return self.val < other.val

        setattr(ListNode, "__lt__", my_lt)

        for l in lists:
            cur_node = l
            while cur_node:
                temp = cur_node
                cur_node = cur_node.next
                temp.next = None
                heapq.heappush(hp, [temp.val, temp])

        dummy_node = ListNode(-1)

        prev_node = dummy_node

        while hp:
            _, cur_node = heapq.heappop(hp)
            prev_node.next = cur_node
            prev_node = cur_node

        return dummy_node.next
