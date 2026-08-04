class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sums = [0] * (len(arr) + 1)
        loc_sum = 0
        for i in range(len(arr)):
            loc_sum += arr[i]
            prefix_sums[i+1] = loc_sum
        
        l = 0
        r = l + k
        res = 0
        while r < len(prefix_sums):
            if (prefix_sums[r] - prefix_sums[l])/k >= threshold:
                res += 1
            r += 1
            l += 1
        return res

