from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        output = 0
        seen = set()

        for x in count.keys():
            if x in seen:
                continue
            elif k - x == x:
                output += count[x] // 2
            elif k - x in count.keys():
                output += min(count[x], count[k - x])
            seen.add(x)
            seen.add(k - x)

        return output
