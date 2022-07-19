class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for _, v in enumerate(s):
            if v.isspace():
                continue
            if v.isalnum():
                new_string += v.lower()

        l, r = 0, len(new_string) - 1
        print(new_string)
        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True
