class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)

        leftTotal, rightTotal = 0, 0

        for l in range(len(nums)):
            leftTotal += nums[l]
            leftSum[l] = leftTotal

        for r in range(len(nums)-1, -1, -1):
            rightTotal += nums[r]
            rightSum[r] = rightTotal

        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1