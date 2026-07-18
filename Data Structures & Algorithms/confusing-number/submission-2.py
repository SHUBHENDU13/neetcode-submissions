class Solution:
    def confusingNumber(self, n: int) -> bool:
        validRotationNums = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        original_n = n
        new_num = 0
        while n:
            digit = n%10
            if digit not in validRotationNums:
                return False
            new_num = 10 * new_num + validRotationNums[digit]
            n //= 10
        return True if new_num != original_n else False