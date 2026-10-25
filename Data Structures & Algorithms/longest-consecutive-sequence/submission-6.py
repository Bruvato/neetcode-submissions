class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2, 20, 4, 10
        # 2 -> 1
        # 3 -> 1 + 1 = 2

        s = set(nums)
        res = 0

        for num in s:
            count = 1

            prev = num - 1
            if num + 1 not in s:
                while prev in s:
                    count += 1
                    prev = prev - 1
            
            res = max(res, count)

        return res