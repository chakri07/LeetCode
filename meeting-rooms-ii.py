'''
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


https://leetcode.com/problems/meeting-rooms-ii
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        
        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,interval[1])
            
        return len(heap)