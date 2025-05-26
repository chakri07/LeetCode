"""
Given an integer array num sorted in non-decreasing order.

You can perform the following operation any number of times:

Choose two indices, i and j, where nums[i] < nums[j].
Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
Return the minimum length of nums after applying the operation zero or more times.

https://leetcode.com/problems/minimum-array-length-after-pair-removals/
"""


# Binary search
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n // 2
        left = 0
        right = mid
        pairs = 0

        while left < mid and right < n:
            if nums[left] < nums[right]:
                left += 1
                pairs += 1
            right += 1
        
        return n - pairs * 2
        

# very slow but one solution
from collections import defaultdict
import heapq
from typing import List
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        heap = []
        
        for freq in freq_map.values():
            heapq.heappush(heap, -1 * freq)

        while len(heap) > 1:
            max_1 = heapq.heappop(heap)
            max_2 = heapq.heappop(heap)

            max_1 += 1
            max_2 += 1
            if max_1 < 0:
                heapq.heappush(heap, max_1)

            if max_2 < 0:
                heapq.heappush(heap, max_2)

        if heap:
            return -1 * heapq.heappop(heap)
        
        return 0

