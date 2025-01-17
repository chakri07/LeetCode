'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

# using sorting 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map: 
                freq_map[num] +=1
            else:
                freq_map[num] = 1

        # now sort the frequ_map 

        sorted_freq_map = dict(sorted(freq_map.items(),
            key = lambda item: item[1],
            reverse = True))

        print(sorted_freq_map)

        return list(sorted_freq_map.keys())[:k]


# solution 2


import collections
import heapq
from typing import List

# heap takes only constant space O(1)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = collections.defaultdict(int)
        
        for num in nums:
            freq_map[num] +=1 
            
        heap = [(freq_map[nums[0]],nums[0])]
        heapq.heapify(heap)
        
        
        for key,val in list(freq_map.items())[1:]:
            if len(heap) < k:
                heapq.heappush(heap,(val,key))
            else:
                min_val,min_key = heap[0]
                if val > min_val:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(val,key))
        ans = []
        for tup in heap:
            ans.append(tup[1])
            
            
        return ans
        
        