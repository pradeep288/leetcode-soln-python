class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the lenght of list A
        len_a = 0
        cur = headA
        while cur:
            cur = cur.next
            len_a += 1

        # find the length of listb
        len_b = 0
        cur = headB
        while cur:
            cur = cur.next
            len_b += 1

        # identify which is max
        new_b, new_a = None, None
        print(len_a, len_b)
        if len_a > len_b:
            offset = len_a - len_b
            cur = headA
            while offset>0:
                cur = cur.next
                offset -= 1
            new_a = cur
            new_b=headB
        else:
            offset = len_b - len_a
            cur = headB
            while offset>0:
                cur = cur.next
                offset -= 1
            new_b = cur
            new_a=headA

        # run until intersection point is reached or null
        while new_a != new_b:
            new_b = new_b.next
            new_a = new_a.next

        return new_a
