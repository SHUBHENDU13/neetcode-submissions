class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i):
            if sum(comb) == target:
                res.append(comb.copy())
                return

            if i >= len(nums) or sum(comb) > target:
                return

            comb.append(nums[i])
            backtrack(i)

            comb.pop()
            backtrack(i + 1)

        backtrack(0)
        return res