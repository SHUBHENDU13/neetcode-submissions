class Solution:
    def longestPalindrome(self, s: str) -> str:
        pos = {}
        length = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = max(length, (r - l + 1))
                l -= 1
                r += 1
            pos[(r - l + 1)] = [l + 1, r - 1]

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = max(length, (r - l + 1))
                l -= 1
                r += 1
            pos[(r - l + 1)] = [l + 1, r - 1]

        maxkey = max(pos)
        l, r = pos[maxkey]
        return s[l:r+1]
                