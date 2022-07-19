class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word.capitalize() == word:
            return True

        return False
