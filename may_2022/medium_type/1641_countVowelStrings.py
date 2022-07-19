class Solution:
    def countVowelStrings(self, n: int) -> int:
        def helper(i, vowel):
            if i == 0:
                return 1

            res = 0
            for x in range(vowel, 5):
                res += helper(i - 1, x)
            return res

        return helper(n, 0)
