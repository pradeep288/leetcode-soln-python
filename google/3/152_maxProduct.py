class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        running_prod, max_product = 1, float('-inf')

        for i in range(len(nums)):
            if nums[i] == 0:
                running_prod = 1
            else:
                running_prod *= nums[i]
            max_product = max(running_prod, max_product)

        running_prod=1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                running_prod = 1
            else:
                running_prod *= nums[i]
            max_product = max(running_prod, max_product)

        return max_product
