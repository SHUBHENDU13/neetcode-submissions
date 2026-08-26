class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        comb = []

        def backtrack(i):
            if i == len(nums):
                res.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(i + 1)
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res