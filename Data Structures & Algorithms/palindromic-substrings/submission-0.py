class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            l, r = i, i
            res1 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res1 += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            res2 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res2 += 1
                l -= 1
                r += 1
            
            res += (res1 + res2)
        
        return res