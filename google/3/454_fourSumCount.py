from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                freq[-1 * s] += 1
        count = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                count += freq[nums3[i] + nums4[j]]

        return count
