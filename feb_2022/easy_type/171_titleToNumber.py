class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        counter = len(columnTitle) - 1
        for c in columnTitle:
            res += pow(26, counter) * (ord(c) - 64)
            counter -= 1

        return res
