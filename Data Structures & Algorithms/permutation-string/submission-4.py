class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c in s1:
            hashmap[c] = 1 + hashmap.get(c, 0)
        # ref copy to restore to original hashmap
        ref_hashmap = hashmap.copy()
        for r in range(len(s2)):
            if s2[r] not in hashmap:
                continue
            else:
                # start from where the first element is found in map
                i = r
                while i < len(s2) and s2[i] in hashmap:
                    hashmap[s2[i]] -= 1
                    # delete keys if value is 0
                    if hashmap[s2[i]] == 0:
                        del hashmap[s2[i]]
                    i += 1
                # move r to current i
                r = i
                if not hashmap:
                    return True
                else:
                    # is answer is not found, restore hashmap using copy
                    hashmap = ref_hashmap.copy()
        return False
        