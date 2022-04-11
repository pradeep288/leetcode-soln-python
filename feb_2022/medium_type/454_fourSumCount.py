class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int],
                     nums4: List[int]) -> int:
        hash_map = {}
        res = 0
        for i in nums1:
            for j in nums2:
                if i + j in hash_map.keys():
                    hash_map[i + j] = 1
                else:
                    hash_map[i + j] += 1

        for i in nums3:
            for j in nums4:
                s = (i + j) * -1
                if s in hash_map.keys():
                    res += 1

        return res
