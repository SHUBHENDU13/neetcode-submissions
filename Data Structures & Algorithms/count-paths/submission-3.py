class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow = [0] * n

        for r in range(m-1,-1,-1):
            currow = [0] * n
            currow[n-1] = 1
            for c in range(n-2,-1,-1):
                currow[c] = currow[c+1] + prevrow[c]
            prevrow = currow
        return prevrow[0]