class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        hm = defaultdict(list)
        # hash table -> string groups

        for s in strs:
            ht = [0] * 26
            
            for c in s:
                ht[ord(c) - ord('a')] += 1
            
            hm[tuple(ht)].append(s)
        
        return list(hm.values())