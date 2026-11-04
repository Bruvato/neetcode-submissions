class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        n = len(nums)

        for r in range(n):
            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r)) # num -> idx
            while q[0][1] <= r - k:
                q.popleft()
            
            if r + 1 >= k:
                res.append(q[0][0])
        return res