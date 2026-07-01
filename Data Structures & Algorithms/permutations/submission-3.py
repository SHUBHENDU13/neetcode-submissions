class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, comb):
            if not nums:
                res.append(comb.copy())
                return

            for i in range(len(nums)):
                comb.append(nums[i])
                dfs(nums[0:i] + nums[i+1:], comb)
                comb.pop()

        dfs(nums, [])
        return res