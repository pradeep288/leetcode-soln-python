class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, rem, a_len, b_len = 0, 0, len(a)-1, len(b)-1
        res = ""
        while a_len >= 0 or b_len >= 0:
            cur_sum = carry
            if a_len >= 0:
                cur_sum += int(a[a_len])
                a_len -= 1
            if b_len >= 0:
                cur_sum += int(b[b_len])
                b_len -= 1
            rem = cur_sum % 2
            carry = cur_sum // 2
            res += str(rem)
        if carry:
            res += str(carry)
        return res[::-1]
