class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                return True
        return False

        