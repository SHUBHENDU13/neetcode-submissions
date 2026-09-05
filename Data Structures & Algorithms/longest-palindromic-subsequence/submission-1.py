class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            if s[i] == s[j]:
                res = dp(i + 1, j - 1) + 2
            else:
                res = max(dp(i + 1, j), dp(i, j - 1))
            cache[(i, j)] = res
            return cache[(i, j)]

        return dp(0, len(s)-1)