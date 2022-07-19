class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, s = 0, 0
        new_head = ListNode(-1)
        cur_node = new_head
        while l1 and l2:
            s = 0
            s += l1.val
            s += l2.val
            s += carry

            new_val = s % 10
            carry = s // 10

            if new_head.val == -1:
                new_head.val = new_val
            else:
                cur_node.next = ListNode(new_val)
                cur_node = cur_node.next

            l1 = l1.next
            l2 = l2.next

        print(carry)
        s = 0
        while l1:
            s = 0
            s += l1.val
            s += carry
            new_val = s % 10
            carry = s // 10
            cur_node.next = ListNode(new_val)
            cur_node = cur_node.next
            l1 = l1.next

        while l2:
            s = 0
            s += l2.val
            s += carry
            new_val = s % 10
            carry = s // 10
            cur_node.next = ListNode(new_val)
            cur_node = cur_node.next
            l2 = l2.next

        if carry:
            cur_node.next = ListNode(carry)

        return new_head