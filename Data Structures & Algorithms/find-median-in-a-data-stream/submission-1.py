class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h1, -num)

        if self.h1 and self.h2 and -self.h1[0] > self.h2[0]:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        if len(self.h1) - len(self.h2) > 1:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        if len(self.h2) - len(self.h1) > 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))
        
        # print(self.h1)
        # print(self.h2)
            

    def findMedian(self) -> float:

        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0]) / 2
        elif len(self.h1) > len(self.h2):
            return -self.h1[0]
        else:
            return self.h2[0]
        
        