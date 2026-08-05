class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c in s1:
            hashmap[c] = 1 + hashmap.get(c, 0)
        ref_hashmap = hashmap.copy()
        for r in range(len(s2)):
            if s2[r] not in hashmap:
                continue
            else:
                i = r
                while i < len(s2) and hashmap and s2[i] in hashmap:
                    hashmap[s2[i]] -= 1
                    if hashmap[s2[i]] == 0:
                        del hashmap[s2[i]]
                    i += 1
                r = i
                if not hashmap:
                    return True
                else:
                    hashmap = ref_hashmap.copy()
        return False
        