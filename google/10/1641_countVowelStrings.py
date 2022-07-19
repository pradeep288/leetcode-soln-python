class Solution:
    def countVowelStrings(self, n: int) -> int:
        res = 0

        def helper(vowel, l):
            nonlocal res
            if l == 0:
                res += 1
                return

            for v in range(vowel, 5):
                helper(v, l - 1)

        helper(0, n)
        return res
