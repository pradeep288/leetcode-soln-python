from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c.most_common(1)[0][0])


        return 0