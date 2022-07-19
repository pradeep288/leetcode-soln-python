class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, cur_str):
            if idx == len(digits):
                res.append(cur_str)
                return
            for c in digit_to_letter[digits[idx]]:
                backtrack(idx+1, cur_str+c)

        if digits:
            backtrack(0, "")

        return res
