class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)


        hm = {}

        res = 0

        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1

        for c in hm:
            print(c)
            count = k
            r = 0
            l = 0

            while r < n:
                if s[r] == c:
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    if count > 0:
                        count -= 1
                        res = max(res, r - l + 1)
                        r += 1
                    else:
                        if s[l] != c:
                            count = min(count + 1, k)
                        l += 1
                        r = max(r, l)
                print(l, r)
            

        return res
        
        # 0 1 2 3 4 5 6 7 8 9 1011
        # A A A A A B B B B C B B