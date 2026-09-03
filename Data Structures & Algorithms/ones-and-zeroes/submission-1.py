class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        count = [[s.count('0'), s.count('1')] for s in strs]

        def dp(i, zeros, ones):
            if i == len(strs):
                return 0

            if (i, zeros, ones) in cache:
                return cache[(i, zeros, ones)]
            
            res = dp(i + 1, zeros, ones)
            z, o = count[i]
            if zeros + z <= m and ones + o <= n:
                res = max(res, (1 + dp(i + 1, zeros + z, ones + o)))
            cache[(i, zeros, ones)] = res
            return res

        return dp(0,0,0)