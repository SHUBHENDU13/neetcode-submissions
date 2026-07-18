class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = {}
        for i in range(len(nums2)):
            pos[nums2[i]] = i
        res = []
        for i in range(len(nums1)):
            res.append(pos[nums1[i]])
        return res