'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
https://leetcode.com/problems/product-of-array-except-self
'''
# O(n) time and O(N) space
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        if len(nums) == 0:
            return 0
        
        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        right[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        
        ans = []
        for i in range(0,len(nums)):
            ans.append(left[i]* right[i])
        
        return ans
    
#  what is an O(1) space solution?

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [0] * len(nums)
        
        ans[0] = 1
        
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
            
        r = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * r
            r = r * nums[i]
            
        return ans