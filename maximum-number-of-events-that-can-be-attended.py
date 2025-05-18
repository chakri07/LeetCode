"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended
"""

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # Sort events by start day
        min_heap = []
        day = 0
        i = 0
        n = len(events)
        attended = 0

        while i < n or min_heap:

            while i < n and  events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
            
            day += 1 


        return attended
