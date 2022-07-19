class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1
            while left < right:
                s = arr[i] + arr[left] + arr[right]
                if s == target:
                    res += 1
                if s > target:
                    right = -1
                else:
                    left += 1

        return res
