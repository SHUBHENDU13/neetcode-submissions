class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r)//2
            time = sum(math.ceil(banana/mid) for banana in piles)
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l