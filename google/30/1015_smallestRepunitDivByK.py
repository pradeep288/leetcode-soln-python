class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in {1, 3, 7, 9}:
            return -1

        num = 1
        length = 1
        while True:
            if num % k == 0:
                return length
            num = num * 10 + 1
            length += 1
