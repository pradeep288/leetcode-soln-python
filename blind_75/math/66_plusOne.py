class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        a = 1
        for i in range(len(digits)-1, -1, -1):
            total = digits[i] + a
            digits[i] = total % 10
            a = total//10

        if a:
            return [a] + digits
        return digits
