"""

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 


https://leetcode.com/problems/network-delay-time
"""

import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v ,t in times:
            graph[u].append((v,t))

        # time, node
        heap = [(0,k)]

        min_cost = defaultdict(lambda: float('inf'))
        min_cost[k] = 0

        while heap:
            curr_time, curr_node = heapq.heappop(heap)

            # Optimization: If we've already found a shorter path to curr_node, skip
            if curr_time > min_cost[curr_node]:
                continue

            for neigh, time_to_neigh in graph[curr_node]:
                new_time = time_to_neigh + curr_time
                if new_time < min_cost[neigh]: # Correct Dijkstra update condition
                    min_cost[neigh] = new_time
                    heapq.heappush(heap, (new_time, neigh))

        # After the loop, check if all nodes have been reached
        if len(min_cost) == n:
            return max(min_cost.values())
        else:
            return -1
