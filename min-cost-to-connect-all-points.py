"""

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

https://leetcode.com/problems/min-cost-to-connect-all-points
"""
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # so no circles we have to do a tree
        # greedy might not work
        n = len(points)

        heap = [(0,0)]

        in_mst = [False] * n 

        mst_cost = 0 

        edges_used = 0 

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            if in_mst[curr_node]:
                continue
            
            in_mst[curr_node] = True
            mst_cost += weight
            edges_used+= 1

            for next_node in range(n):
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0]- points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost
