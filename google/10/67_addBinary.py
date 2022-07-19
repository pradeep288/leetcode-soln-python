class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = sorted(a, reverse=True)
        b = sorted(b, reverse=True)

        res = []

        i, j = 0, 0
        carry = 0
        while i < len(a) or j < len(b):
            s = carry
            if i < len(a):
                s += int(a[i])
                i += 1
            if j < len(b):
                s += int(b[i])
                j += 1
            res.append(str(s % 2))
            carry = s / 2
        if carry:
            res.append(carry)
        return "".join(res[::-1])
