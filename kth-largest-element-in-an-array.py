'''

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

https://leetcode.com/problems/kth-largest-element-in-an-array/
'''

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        heap = [nums[0]]
        heapq.heapify(heap)
        
        for num in nums[1:]:
            if len(heap) < k:
                heapq.heappush(heap,num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)
                    
        return heap[0]