class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        comb = []

        def backtrack(i):
            if i == len(s):
                res.append(comb.copy())
                return

            for j in range(i, len(s)):
                if isPali(i, j):
                    comb.append(s[i:j+1])
                    backtrack(j + 1)
                    comb.pop()
        
        def isPali(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        backtrack(0)
        return res