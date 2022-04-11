'''
class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num >= 0:
            digital_root += num % 10
            num //= 10

            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0

        return digital_root
'''


class Solution:
    def addDigits(self, num: int) -> int:
        if num<9:
            return num

        if num % 9 == 0:
            return 9
        return num % 9
