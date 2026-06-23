import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = []
        adj_list = defaultdict(list)

        # neigh, price
        for fro,to,price in flights:
            adj_list[fro].append((to,price))

        cost_arr = [float('inf')] * n
        cost_arr[src] = 0 

        # stops, price, source
        heapq.heappush(heap,(0, 0, src))

        while heap:
            stops, curr_cost, curr_city= heapq.heappop(heap)
            next_cities = adj_list[curr_city]

            if stops > k:
                break

            for city,cost in next_cities:
                if cost_arr[city] > curr_cost + cost:
                    cost_arr[city] = curr_cost + cost
                    heapq.heappush(heap,(stops+1, curr_cost + cost, city))



        return -1 if cost_arr[dst] == float('inf') else cost_arr[dst]
        