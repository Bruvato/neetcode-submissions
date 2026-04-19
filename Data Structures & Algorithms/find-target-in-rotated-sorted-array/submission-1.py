class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if nums[l] < target < nums[mid] or target < nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
            


        if nums[l] != target:
            return -1
        
        return l