class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for c in s:
            if c == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    element = stack.pop()
                    temp = element + temp
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(temp * int(k))
            else:
                stack.append(c)
        return "".join(stack)
