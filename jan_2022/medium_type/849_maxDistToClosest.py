class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l_to_r, r_to_l = [0] * len(seats), [0] * len(seats)

        if seats[0] == 0:
            l_to_r[0] = float('inf')
        for i in range(1, len(l_to_r)):
            if seats[i] == 0:
                l_to_r[i] = l_to_r[i - 1] + 1

        if seats[len(seats) - 1] == 0:
            r_to_l[len(seats) - 1] = float('inf')
        for i in range(len(seats) - 2, -1, -1):
            if seats[i] == 0:
                r_to_l[i] = r_to_l[i + 1] + 1

        res = float('-inf')
        for i in range(len(seats)):
            temp = min(l_to_r[i], r_to_l[i])
            res = max(temp, res)

        return res
