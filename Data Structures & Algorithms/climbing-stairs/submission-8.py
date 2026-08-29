class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def backtrack(i):
            if i == n:
                return 1
            if i > n:
                return 0

            if i in dp.keys():
                return dp[i]

            onestep = backtrack(i + 1)
            twostep = backtrack(i + 2)
            dp[i] = onestep + twostep
            return dp[i]

        return backtrack(0)