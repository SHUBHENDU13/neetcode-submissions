class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        ans = 0
        while l <= r:
            mid = (l+r)//2
            curr = mid*mid
            if curr > num:
                r = mid-1
            elif curr < num:
                l = mid+1
            else:
                ans = mid
                break
        return True if ans > 0 else False
            