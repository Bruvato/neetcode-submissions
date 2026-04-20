class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)

        res = []
        heap = []

        for i in range(n):
            point = points[i]
            x, y = point
            dist = math.sqrt(x * x + y * y)

            heap.append((dist, point))
        
        heapq.heapify(heap)
        
        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)


        return res