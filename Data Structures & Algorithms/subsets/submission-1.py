class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

        # do not include current element
        self.helper(i+1, nums, curset, subset)