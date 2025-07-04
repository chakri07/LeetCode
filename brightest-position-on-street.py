"""
https://leetcode.com/problems/brightest-position-on-street
"""

import heapq
from typing import List

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        
        lanterns = sorted(lights, key = lambda x: x[0] - x[1])

        cones = []
        for p, r in lanterns:
            cones.append((p - r, p + r))

        heapq.heapify(cones)
        start, end = heapq.heappop(cones)
        concurrent = []
        heapq.heappush(concurrent, (end, start))
        ans = start
        light = 1
        while cones:
            start, end = heapq.heappop(cones)
            if concurrent and concurrent[0][0] >= start:
                maxb = len(concurrent) + 1
                pos = start
                if maxb > light:
                    light = maxb
                    ans = pos
            else:
                while concurrent and concurrent[0][0] < start:
                    heapq.heappop(concurrent)
            heapq.heappush(concurrent, (end, start))
        
        return ans
