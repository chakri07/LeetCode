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
# inplace 
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick_select(l,r):
            if l == r:
                return nums[l]

            pivot_idx = random.randint(l,r)
            
            pivot, p = nums[pivot_idx], l

            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p] , nums[i]
                    p+= 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quick_select(l,p-1)
            if k > p:
                return quick_select(p+1,r)
            
            return nums[p]

        return quick_select(0,len(nums)-1)

# Horase algorithm
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)


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