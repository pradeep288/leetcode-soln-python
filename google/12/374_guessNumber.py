class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            m = l + ((r - l) // 2)
            res = guess(m)
            if res == 0:
                return m
            elif res < 0:
                r = m - 1
            else:
                l = m + 1

        return -1
