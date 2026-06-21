import heapq
class MedianFinder:

    def __init__(self):
        self.lower_heap = [] # max_heap 
        self.upper_heap = [] # min_heap 
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        # push into lower heap first
        heapq.heappush(self.lower_heap, -num)

        # then push the biggest one into minheap upper
        num = -heapq.heappop(self.lower_heap)
        heapq.heappush(self.upper_heap, num)

        # len lower heap is equal or +1 than upper heap
        if len(self.upper_heap) > len(self.lower_heap):
            num = heapq.heappop(self.upper_heap)
            heapq.heappush(self.lower_heap, -num)
        

    def findMedian(self) -> float:
        # if odd
        if self.length % 2 == 1:
            return -self.lower_heap[0]
        else:
            return (-self.lower_heap[0] + self.upper_heap[0])/2




        
        