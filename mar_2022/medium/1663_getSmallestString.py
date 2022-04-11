class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = n * ["a"]
        k = k - n

        i = n - 1
        while i >= 0:
            if k > 25:
                k = k - 25
                res[i] = 'z'
                i -= 1
            else:
                res[i] = chr(97 + k)
                break

        return "".join(res)
