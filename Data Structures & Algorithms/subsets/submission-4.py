class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(i):
            if i == len(nums):
                res.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(i + 1)
            comb.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res