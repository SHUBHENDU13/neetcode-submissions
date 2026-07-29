class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        diff = (arr[-1] - arr[0])//len(arr)
        expected = arr[0]
        for val in arr:
            if val != expected:
                return expected
            
            expected += diff
        return expected