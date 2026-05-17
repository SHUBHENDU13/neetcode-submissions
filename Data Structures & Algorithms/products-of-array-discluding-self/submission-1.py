class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix, postfix = 1, 1

        for i in range(len(res)):
            res[i] = res[i] * prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res

        

        
