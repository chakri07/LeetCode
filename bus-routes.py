"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

https://leetcode.com/problems/bus-routes/
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        
        # stop will store all the route indices its in 
        graph = defaultdict(list)
        
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].append(i)

        queue = deque([])
        visited = set()

        for route_idx in graph[source]:
            queue.append((route_idx,1))
            visited.add(route_idx)

        while queue:
            curr_route_idx, num_buses = queue.popleft()

            for stop in routes[curr_route_idx]:
                if stop == target:
                    return num_buses
                
                for next_idx in graph[stop]:
                    if next_idx not in visited:
                        queue.append((next_idx, num_buses+1 ))
                        visited.add(next_idx)


        return -1




from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0
        graph = defaultdict(list)

        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].append(i)

        queue = deque()
        visited = set()

        for route in graph[source]:
            queue.append(route)
            visited.add(route)
        
        ans = 1

        while queue:
            n = len(queue)
            for j in range(n):
                route_idx = queue.popleft()
                route = routes[route_idx]
                for stop in route:
                    if stop == target:
                        return ans 

                    for next_route_idx in graph[stop]:
                        if not next_route_idx in visited:
                            visited.add(next_route_idx)
                            queue.append(next_route_idx)
            
            ans +=1 


        return -1