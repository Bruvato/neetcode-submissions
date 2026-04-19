class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0
        r = 0

        seen = set()
        res = 0

        while r < n:
            cr = s[r]
            cl = s[l]

            if cr not in seen:
                seen.add(cr)
                res = max(res, r - l + 1)
                r += 1
            else:
                seen.remove(cl)
                l += 1

            print(l, r)
        
        return res 

        # l
        #   r
        # a b b a


        