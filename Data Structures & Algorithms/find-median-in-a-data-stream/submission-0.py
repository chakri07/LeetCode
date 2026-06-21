import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # For smaller half (use negative values for max heap)
        self.min_heap = []  # For larger half

    
    def addNum(self, num: int) -> None:

        # Add to max_heap (negate for max behavior with min heap)
        heapq.heappush(self.max_heap, -num)

        # Move the largest element from max_heap to min_heap
        largest_small = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_small)

        # Balance the heaps - max_heap should have equal or one more element
        if len(self.min_heap) > len(self.max_heap):
            smallest_large = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_large)
    
    
    def findMedian(self) -> float:
        """
        Returns the median of all elements so far.
        
        If odd number of elements: return top of max_heap
        If even number of elements: return average of both heap tops
        """
        if len(self.max_heap) > len(self.min_heap):
            # Odd number of elements, median is top of max_heap
            return float(-self.max_heap[0])
        else:
            # Even number of elements, median is average of both tops
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
