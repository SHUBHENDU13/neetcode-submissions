class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i, target):
            while i * i <= target:
                if target % i == 0:
                    res.append(comb + [i, target // i])
                    comb.append(i)
                    backtrack(i, target // i)
                    comb.pop()
                i += 1

        backtrack(2, n)
        return res
