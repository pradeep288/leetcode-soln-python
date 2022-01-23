class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high, ans = 0, max(piles) - 1, 0

        while low <= high:
            mid = (low + high) // 2
            if self.eat_possible(piles, high, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def eat_possible(self, piles, high, mid):
        count = 0
        for pile in piles:
            if pile <= mid:
                count += 1
            else:
                count = count + pile // mid
                if pile % mid:
                    count += 1
        return count <= high
