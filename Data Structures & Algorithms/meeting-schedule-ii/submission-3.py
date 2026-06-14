"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        rooms = 1

        heap = [intervals[0].end]
        # by default its min heap, we can change it by adding - sign to it

        heapq.heapify(heap)

        for inter in intervals[1:]:
            if heap[0] <= inter.start:
                heapq.heappop(heap)
            heapq.heappush(heap,inter.end)

        return len(heap)