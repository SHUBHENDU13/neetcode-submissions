class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def backtrack(step):
            if step == n:
                return 1
            if step > n:
                return 0
            
            if step in dp.keys():
                return dp[step]

            onestep = backtrack(step + 1)
            twostep = backtrack(step + 2)
            dp[step] = onestep + twostep
            return dp[step]

        return backtrack(0)