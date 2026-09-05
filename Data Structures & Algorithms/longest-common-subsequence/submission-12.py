class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        cache = {}

        def dp(i1, i2):
            if i1 == N or i2 == M:
                return 0

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            result = 0
            if text1[i1] == text2[i2]:
                result = 1 + dp(i1 + 1, i2 + 1)
            else:
                result = max(dp(i1 + 1, i2), dp(i1, i2 + 1))
            cache[(i1, i2)] = result
            return cache[(i1, i2)]

        return dp(0,0)

