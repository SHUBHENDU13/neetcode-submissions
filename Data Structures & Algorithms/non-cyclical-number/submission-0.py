class Solution:
    def isHappy(self, n: int) -> bool:
        numset = set()
        
        def dfs(n):
            if n == 1:
                return True

            newsum = 0
            while n > 0:
                digit = n % 10
                newsum += digit * digit
                n = n // 10
            if newsum in numset:
                return False
            numset.add(newsum)
            return dfs(newsum)

        return dfs(n)
            