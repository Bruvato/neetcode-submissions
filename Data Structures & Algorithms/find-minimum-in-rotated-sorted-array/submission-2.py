class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        n = len(nums)

        l = 0
        r = n -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] <= nums[0]:
                res = min(res, nums[mid])
                r = mid - 1
                res = min(res, nums[r])

        
        return res
    # 3, 4, 5, 6, 1, 2
    #          l  m  r


    # 4, 5, 0, 1, 2, 3
    # l  r           
    # m


