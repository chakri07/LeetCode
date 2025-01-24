"""

Non-overlapping Intervals
Solved 
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[2,4]]

Output: 0
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000

https://neetcode.io/problems/non-overlapping-intervals
"""

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
