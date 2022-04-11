class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, mx =[], 0
        