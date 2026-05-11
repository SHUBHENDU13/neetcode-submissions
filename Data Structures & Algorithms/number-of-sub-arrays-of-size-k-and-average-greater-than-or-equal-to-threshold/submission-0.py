class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = 0
        ans = 0
        L = 0

        for R in range(len(arr)):
            windowSum += arr[R]
            if R - L + 1 > k:
                windowSum -= arr[L]
                L += 1
            if R - L + 1 == k:
                if windowSum/k >= threshold:
                    ans += 1
        return ans