class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # newArr = [0] * 2 * len(nums)
        # k = 0
        # for i in range(len(nums)):
        #     newArr[k] = nums[i]
        #     k += 1

        # for i in range(len(nums)):
        #     newArr[k] = nums[i]
        #     k += 1 

        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        
        return ans