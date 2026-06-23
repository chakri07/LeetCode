import heapq
from collections import defaultdict 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj_list = defaultdict(list)

        n = len(points)
        for i in range(0,n) :
            p1x, p1y = points[i]
            for j in range(i+1, len(points)):
                p2x, p2y = points[j]
                dist = abs(p1x-p2x) + abs(p1y - p2y)
                adj_list[i].append([dist,j])
                adj_list[j].append([dist,i])

        res  = 0 
        visit = set()
        # cost , idx
        heap =[[0,0]]

        while len(visit) < len(points):
            cost, idx = heapq.heappop(heap)
            if idx in visit:
                continue
            res += cost
            visit.add(idx)
            for neiCost, nei in adj_list[idx]:
                heapq.heappush(heap,[neiCost,nei])


        return res



        