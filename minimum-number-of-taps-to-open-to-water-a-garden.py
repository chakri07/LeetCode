"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e., the length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.


Example 1:

Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
 

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden
"""

import heapq # Not needed for the greedy approach, but keeping it if you want to reuse structure
from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Step 1: Preprocess to find the maximum reach from each starting point
        # max_reach[i] will store the furthest point reachable if we start covering from point 'i'
        max_reach = [0] * (n + 1) 

        for i in range(n + 1):
            # Calculate the tap's coverage interval [start, end]
            start = max(0, i - ranges[i])
            end = i + ranges[i]
            
            # If a tap covers 'start', it can reach up to 'end'.
            # We want to record the maximum 'end' achievable from 'start'.
            # Note: A single tap might cover multiple 'start' points, but we only care about its
            # effective starting point. The loop ensures we pick the best 'end' for each 'start'.
            max_reach[start] = max(max_reach[start], end)

        # Step 2: Greedy selection of taps
        taps = 0
        current_covered_end = 0  # Represents how far we have covered from 0
        next_possible_reach = 0 # Represents the maximum reach we can achieve using taps selected so far


        for i in range(n + 1):
            if i > next_possible_reach:
                return -1
            
 
            if i > current_covered_end:
                taps += 1
                current_covered_end = next_possible_reach

            next_possible_reach = max(next_possible_reach, max_reach[i])
        
        # After iterating through all points, if the entire garden [0, n] is covered,
        # next_possible_reach should be at least 'n'.
        if next_possible_reach < n:
            return -1 # Still a gap at the end

        return taps
