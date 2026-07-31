class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, suf_prod = [1] * len(nums), [1] * len(nums)
        
        for i in range(len(nums)-1):
            pre_prod[i+1] = pre_prod[i] * nums[i]
        
        for i in range(len(nums)-1, 0, -1):
            suf_prod[i-1] = suf_prod[i] * nums[i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre_prod[i] * suf_prod[i]

        return res

