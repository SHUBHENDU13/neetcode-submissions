class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        
        def dp(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = dp(i1 + 1, i2 + 1)
                return 1 + cache[(i1, i2)]
            else:
                cache[(i1 + 1, i2)] = dp(i1 + 1, i2)
                cache[(i1, i2 + 1)] = dp(i1, i2 + 1)
                return max(cache[(i1 + 1, i2)], cache[(i1, i2 + 1)])

        return dp(0,0)