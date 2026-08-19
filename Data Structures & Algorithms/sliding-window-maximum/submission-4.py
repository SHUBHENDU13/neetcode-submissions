class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # [val, index]
        for r, num in enumerate(nums):
            while q and q[-1][0] < num:
                q.pop()
            q.append([num, r])

            while q and q[0][1] <= r - k:
                q.popleft()

            if r >= k - 1:
                output.append(q[0][0])
        return output