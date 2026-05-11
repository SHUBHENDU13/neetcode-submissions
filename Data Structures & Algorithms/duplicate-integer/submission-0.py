class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_set = set(nums)
        if(len(temp_set) != len(nums)):
            return True
        return False
        