class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        count = [[s.count('0'), s.count('1')] for s in strs]

        def dp(i, zeros, ones):
            if i == len(strs):
                return 0

            if (i, zeros, ones) in cache:
                return cache[(i, zeros, ones)]

            cache[(i, zeros, ones)] = dp(i + 1, zeros, ones)
            z, o = count[i]
            if z <= zeros and o <= ones:
                cache[(i, zeros, ones)] = max(cache[(i, zeros, ones)],
                                                1 + dp(i + 1, zeros - z, ones - o))
            return cache[(i, zeros, ones)]

        return dp(0,m,n)
