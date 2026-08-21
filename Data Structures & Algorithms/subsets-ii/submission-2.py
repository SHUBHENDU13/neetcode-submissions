class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # if adding ith element, keep adding
            subset.append(nums[i])
            dfs(i+1, subset)

            # if skipping ith element, skip all same elements
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)

        dfs(0, [])
        return res