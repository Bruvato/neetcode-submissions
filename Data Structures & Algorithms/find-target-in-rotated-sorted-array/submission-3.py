class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)


        l = 0
        r = n - 1

        p = (l+r) // 2

        while l < r:
            if nums[p] < nums[r]:
                r = p
            else:
                l = p + 1
            
            p = (l + r) // 2
        
        if nums[p] <= target <= nums[n - 1]:
            l = p
            r = n - 1
        else:
            l = 0
            r = p - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            
        return -1
