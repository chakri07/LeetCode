import heapq
class MedianFinder:

    def __init__(self):
        self.lower_heap = [] # max_heap 
        self.upper_heap = [] # min_heap 
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        # we always push into max_heap , then push one from max to min heap and then balance
        heapq.heappush(self.lower_heap, -num)
        num = -heapq.heappop(self.lower_heap)
        heapq.heappush(self.upper_heap, num)

        if len(self.upper_heap) > len(self.lower_heap):
            extra = heapq.heappop(self.upper_heap)
            heapq.heappush(self.lower_heap, -extra)

    def findMedian(self) -> float:
        if self.length %2 == 0:
            return (-self.lower_heap[0] + self.upper_heap[0])/2
        else:
            return -self.lower_heap[0] 
        