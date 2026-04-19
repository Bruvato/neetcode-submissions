class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hm = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(n):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxf = max(maxf, hm[s[r]])
            
            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
        
        # 0 1 2 3 4 5 6 7 8 9 1011
        # A A A A A B B B B C B B