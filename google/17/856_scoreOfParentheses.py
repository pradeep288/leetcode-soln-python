class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                val = 0
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(2 * val, 1)
                stack.pop()
                stack.append(val)

        return sum(stack)
