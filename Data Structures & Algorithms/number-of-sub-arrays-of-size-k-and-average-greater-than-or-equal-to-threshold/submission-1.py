class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currTotal = 0
        count = 0
        L = 0

        for R in range(len(arr)):
            currTotal += arr[R]
            if R - L + 1 > k:
                currTotal -= arr[L]
                L += 1
            if R - L + 1 == k and currTotal/k >= threshold:
                count += 1
        return count