class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        hm1 = {}
        hm2 = {}

        for c in s1:
            hm1[c] = hm1.get(c, 0) + 1
        
        for j in range(n):
            hm2[s2[j]] = hm2.get(s2[j], 0) + 1
        
        if hm1 == hm2:
            return True
        
        for i in range(0, m - n):
            
            first = s2[i]
            last = s2[i + n]
            hm2[first] = hm2[first] - 1
            if hm2[first] <= 0:
                del hm2[first]

            hm2[last] = hm2.get(last, 0) + 1

            print(hm1, hm2)

            if hm1 == hm2:
                return True
        
        return False