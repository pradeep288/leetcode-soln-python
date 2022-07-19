class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        res = 0
        while i <= j:
            remain = limit - people[j]
            res += 1
            j-=1
            if remain - people[i] >= 0:
                i += 1
        return res
