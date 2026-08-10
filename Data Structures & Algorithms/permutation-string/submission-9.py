class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seq = {i:0 for i in range(26)}
        for c in s1:
            seq[ord(c) - ord('a')] += 1
        hashmap = {i:0 for i in range(26)}
        l = 0
        for r in range(len(s2)):
            hashmap[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                hashmap[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if r - l + 1 == len(s1):
                if seq == hashmap:
                    return True

        return False