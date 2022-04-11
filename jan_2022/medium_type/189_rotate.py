class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr):
            low, high = 0, len(arr) - 1
            while low < high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
            return arr

        k = k % len(nums)

        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])

        return nums
