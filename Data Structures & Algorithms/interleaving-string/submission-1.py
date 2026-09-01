class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}

        def dp(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            ans = False
            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dp(i1 + 1, i2):
                ans = True
            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dp(i1, i2 + 1):
                ans = True
            cache[(i1, i2)] = ans
            return ans

        return dp(0,0)