class Solution:
    def isValid(self, s: str) -> bool:
        expected = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if stack and stack[-1] == expected[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
