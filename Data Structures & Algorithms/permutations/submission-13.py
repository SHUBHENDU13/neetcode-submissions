class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i):
            if i == len(nums):
                res.append(comb.copy())
                return

            for j in range(len(comb)+1):
                comb.insert(j, nums[i])
                backtrack(i + 1)
                comb.pop(j)

        backtrack(0)
        return res