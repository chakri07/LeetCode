"""
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # end time heap
        end_time_heap = []
        flowers = sorted(flowers, key = lambda x : x[0])
        curr_idx = 0 
        ans = {}
        original = list(people)

        for ppl_time in sorted(people):
            # first remove any that are done blooming 
            while curr_idx < len(flowers) and flowers[curr_idx][0] <= ppl_time:
                heapq.heappush(end_time_heap, flowers[curr_idx][1])
                curr_idx += 1

            while end_time_heap and end_time_heap[0] < ppl_time:
                heapq.heappop(end_time_heap) 


            
            ans[ppl_time] = len(end_time_heap)

        final_ans = []
        for i in range(len(people)):
            final_ans.append(ans[original[i]])

        return final_ans



        
https://leetcode.com/problems/number-of-flowers-in-full-bloom
"""
from typing import List
import heapq
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # end time heap
        end_time_heap = []
        flowers = sorted(flowers, key = lambda x : x[0])
        curr_idx = 0 
        ans = {}
        original = list(people)

        for ppl_time in sorted(people):
            # first remove any that are done blooming 
            while curr_idx < len(flowers) and flowers[curr_idx][0] <= ppl_time:
                heapq.heappush(end_time_heap, flowers[curr_idx][1])
                curr_idx += 1

            while end_time_heap and end_time_heap[0] < ppl_time:
                heapq.heappop(end_time_heap) 


            
            ans[ppl_time] = len(end_time_heap)

        final_ans = []
        for i in range(len(people)):
            final_ans.append(ans[original[i]])

        return final_ans


