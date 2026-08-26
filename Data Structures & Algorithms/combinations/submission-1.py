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

            comb.append(i)
            backtrack(i + 1)

            comb.pop()
            backtrack(i + 1)

        backtrack(1)
        return res