class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0] * (len(nums1) + len(nums2))
        l, r, k = 0, 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                arr[k] = nums1[l]
                l += 1
            else:
                arr[k] = nums2[r]
                r += 1
            k += 1
        while l < len(nums1):
            arr[k] = nums1[l]
            l += 1
            k += 1
        while r < len(nums2):
            arr[k] = nums2[r]
            r += 1
            k += 1
        
        mid = len(arr)//2
        if len(arr)%2 == 0:
            return (arr[mid-1] + arr[mid])/2.0
        else:
            return float(arr[mid])