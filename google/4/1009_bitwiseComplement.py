class Solution:
    def bitwiseComplement(self, n: int) -> int:
        compliment = []
        while n > 0:
            if n & 1 == 1:
                compliment.append(0)
            else:
                compliment.append(1)
            n >>= 1
        res = 0
        print(compliment)
        for k, v in enumerate(compliment):
            res += (2**k)*v

        return res
