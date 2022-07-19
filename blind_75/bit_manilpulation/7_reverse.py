class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0

        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1

        while x > 0:
            rem = x % 10
            x = x // 10
            res = res * 10 + rem
        if res >= 2 ** 31 - 1 or res <= -2 ** 31: return 0

        return res * sign
