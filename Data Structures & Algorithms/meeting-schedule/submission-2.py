"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,key = lambda x: x.start)

        for i in range(0,len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        
        return True
