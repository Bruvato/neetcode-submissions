class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        ns, ne = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]

            if ne < start:
                res.append([ns, ne])
                return res + intervals[i:]
            elif end < ns:
                res.append(intervals[i])
            else:
                ns = min(ns, start)
                ne = max(ne, end)
        
        res.append([ns, ne])
        return res