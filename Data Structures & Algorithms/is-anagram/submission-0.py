class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hs = [0] * 26
        ht = [0] * 26

        for i in range(len(s)):
            hs[ord(s[i]) - ord('a')] += 1
            ht[ord(t[i]) - ord('a')] += 1
        
        print(hs, ht)


        return hs == ht
            