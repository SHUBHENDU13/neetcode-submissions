class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, nums, comb):
            if not nums:
                res.append(comb.copy())
                return

            for i in range(len(nums)):
                comb.append(nums[i])
                dfs(i, nums[0:i] + nums[i+1:], comb)
                comb.pop()

        dfs(0, nums, [])
        return res