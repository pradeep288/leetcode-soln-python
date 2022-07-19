class Solution:
    def greatestLetter(self, s: str) -> str:
        s =sorted(s)
        temp=[]
        for i in range(len(s)):
            temp.append(ord(s[i]))

        for i in range(len(s)-1, -1, -1):
            if temp[i] - 32 in temp:
                return chr(temp[i]-32)

        return ""
