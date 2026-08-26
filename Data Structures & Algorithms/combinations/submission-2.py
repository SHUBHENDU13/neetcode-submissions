class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i):
            if len(comb) == k:
                res.append(comb.copy())
                return

            if i > n:
                return

            for j in range(i, n + 1):
                comb.append(j)
                backtrack(j + 1)
                comb.pop()

        backtrack(1)
        return res