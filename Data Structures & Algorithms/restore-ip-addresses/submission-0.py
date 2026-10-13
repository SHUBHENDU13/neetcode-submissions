class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        comb = []

        def backtrack(i, comb):
            if len(comb) == 4 and i == len(s):
                res.append('.'.join(comb))
                return

            if i >= len(s):
                return

            for j in range(i, min(i + 3, len(s))):
                if j != i and s[i] == '0':
                    continue
                if int(s[i: j+1]) < 256:
                    comb.append(s[i:j + 1])
                    backtrack(j + 1, comb)
                    comb.pop()
        
        backtrack(0, comb)
        return res

        