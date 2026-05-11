class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxOnes = max(maxOnes, count)
                count = 0
        maxOnes = max(maxOnes, count)
        return maxOnes