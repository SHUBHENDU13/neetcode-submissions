class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        speed = max(piles)
        l, r = 1, speed
        while l < r:
            mid = (l + r)//2
            hours = sum(math.ceil(banana/mid) for banana in piles)
            if hours <= h:
                speed = min(speed, mid)
                r = mid
            else:
                l = mid + 1
        return speed