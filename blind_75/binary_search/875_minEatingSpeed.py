import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        res = e

        while s <= e:
            m = s + ((e - s) // 2)
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / m)

            if time <= h:
                res = m
                e = m - 1
            else:
                s = m + 1

        return res
