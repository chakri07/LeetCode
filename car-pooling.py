"""


There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

https://leetcode.com/problems/car-pooling

"""

import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by pick up location 
        # keep track of curr_locations 

        trips = sorted(trips, key = lambda x : x[1])

        print(trips)

        curr_people = 0 

        max_heap = []

        for num,start,end in trips:
            # end
            while max_heap and max_heap[0][0] <= start:
                _, prev_num = heapq.heappop(max_heap)
                curr_people -= prev_num

            curr_people += num

            if curr_people > capacity:
                return False 
            
            heapq.heappush(max_heap,[end,num])

        return True