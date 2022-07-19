class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            tmp = n
            total = 0
            while tmp > 0:
                rem = tmp % 10
                tmp = tmp // 10
                total += rem * rem
            n = total
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
