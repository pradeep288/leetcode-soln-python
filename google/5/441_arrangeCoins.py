class Solution:
    def arrangeCoins(self, n: int) -> int:
        row_len = 0
        while n >= 0:
            row_len += 1
            n = n - row_len

        return row_len-1
