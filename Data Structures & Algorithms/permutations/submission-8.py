class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, comb):
            if not nums:
                res.append(comb.copy())
                return

            for i in range(len(nums)):
                # add the current idx num in comb
                comb.append(nums[i])
                dfs(nums[0:i] + nums[i+1:], comb)
                # remove the current idx num from comb before moving to next num
                comb.pop()

        dfs(nums, [])
        return res