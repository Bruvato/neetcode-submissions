class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        #  0 1 2 3 4 5
        # -1 0 2 4 6 8

        return -1