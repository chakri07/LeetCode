class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals,key = lambda x : x[1])

        n = len(intervals)
        temp_start,temp_end = intervals[0][0], intervals[0][1]
        remove = 0
        for inter in intervals[1:]:
            start,end = inter[0],inter[1]
            if temp_end > start:
                remove += 1
            else:
                temp_start = start
                temp_end = end

        return remove

        
                
        