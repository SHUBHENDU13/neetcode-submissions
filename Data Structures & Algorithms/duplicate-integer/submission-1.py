class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # temp_set = set(nums)
        # if(len(temp_set) != len(nums)):
        #     return True
        # return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

        