class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1

        res = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
            res = max(res, min(heights[l], heights[r]) * (r - l))
        

        return res
