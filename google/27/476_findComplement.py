class Solution:
    def findComplement(self, num: int) -> int:
        res, i = 0, 0
        while num:
            if num & 1 == 0:
                res += 1 << i
            num >>= 1
            i += 1

        return res
