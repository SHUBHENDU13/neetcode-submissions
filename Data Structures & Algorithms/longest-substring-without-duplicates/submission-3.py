class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        L = 0
        length = 0

        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L += 1
            charset.add(s[R])
            length = max(length, R - L + 1)
        
        return length