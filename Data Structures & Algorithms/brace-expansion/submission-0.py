class Solution:
    def expand(self, s: str) -> List[str]:
        hashmap = defaultdict(list)
        i, j = 0, 0
        while i < len(s):
            if s[i] == '{':
                i += 1
                while s[i] != '}':
                    if s[i] == ',':
                        i += 1
                        continue
                    hashmap[j].append(s[i])
                    i += 1
                i += 1
                j += 1
            else:
                hashmap[j].append(s[i])
                i += 1
                j += 1
        res = []
        comb = []

        def backtrack(i):
            if len(comb) == len(hashmap):
                res.append(''.join(comb))
                return
            
            for j in range(len(hashmap[i])):
                comb.append(hashmap[i][j])
                backtrack(i + 1)
                comb.pop()

        backtrack(0)
        return res

            