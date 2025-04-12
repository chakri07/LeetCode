'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''
# bucket sort
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ## Bucket sort
        counts = defaultdict(int)

        max_count = float('-inf')

        for num in nums:
            counts[num] += 1
            max_count = max(max_count, counts[num])
        
        # freq_arr 
        freq_arr = [[] for _ in range(max_count)]
        # print(freq_arr)

        for  num,freq in counts.items():
            freq_arr[freq-1].append(num)

        # print(freq_arr)
        result = []

        for i in range(max_count-1,-1,-1):
            if len(result) == k:
                return result
            
            result.extend(freq_arr[i])

        return result


from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        max_heap = []

        for num,freq in freq_map.items():
            heapq.heappush(max_heap,(-freq, num))

        ans = []
        for _ in range(k):
            if max_heap:
                _, num = heapq.heappop(max_heap)
                ans.append(num)

        return ans

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
        
        