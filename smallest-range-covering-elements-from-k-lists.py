"""

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists
"""
import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        max_val = float('-inf')
        
        range_start = 0 
        range_end = float('inf')

        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0],i,0))
            max_val = max(max_val, nums[i][0])

        while len(pq) == len(nums):
            min_val, row_idx, val_idx = heapq.heappop(pq)

            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val

            # i.e) next number exists
            if val_idx + 1 < len(nums[row_idx]):
                next_val = nums[row_idx][val_idx+1]
                heapq.heappush(pq, (next_val,row_idx, val_idx + 1))
                max_val = max(max_val, next_val)

        return [range_start, range_end]