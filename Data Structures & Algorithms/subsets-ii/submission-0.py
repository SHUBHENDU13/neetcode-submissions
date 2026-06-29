class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curset, subset = [], []
        self.helper(0, nums, curset, subset)
        return subset

    def helper(self, i, nums, curset, subset):
        if i >= len(nums):
            subset.append(curset.copy())
            return

        # include current element
        curset.append(nums[i])
        self.helper(i+1, nums, curset, subset)
        curset.pop()

        # do not include current element and subsequent similar elements
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1, nums, curset, subset)