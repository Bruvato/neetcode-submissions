class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0
        r = 0

        seen = {}
        res = 0

        while r < n:
            if s[r] not in seen or l > seen[s[r]]:
                seen[s[r]] = r
                res = max(res, r - l + 1)
                r += 1
            else:
                l = seen[s[r]] + 1

            print(l, r, res)
        
        return res 

        # l
        #   r
        # a b b a
