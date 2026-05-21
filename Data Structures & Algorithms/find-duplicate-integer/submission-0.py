class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nset = set()

        for n in nums:
            if n in nset:
                return n
            else:
                nset.add(n)
        
        return -1