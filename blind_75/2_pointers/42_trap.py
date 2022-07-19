class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        l_to_r, r_to_l = [0] * N, [0] * N

        left_max = height[0]
        for i in range(1, N):
            temp = height[i]
            l_to_r[i] = left_max
            left_max = max(left_max, temp)

        right_max = height[-1]
        for i in range(N - 2, -1, -1):
            temp = height[i]
            r_to_l[i] = right_max
            right_max = max(right_max, temp)

        res = 0

        for i in range(N):
            if (min(l_to_r[i], r_to_l[i]) - height[i]) >= 0:
                res += min(l_to_r[i], r_to_l[i]) - height[i]

        return res
