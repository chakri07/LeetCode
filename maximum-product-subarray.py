'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


https://leetcode.com/problems/maximum-product-subarray/
'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        curr = pos = neg = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            curr = num
            temp_max = max(curr, pos * curr, neg * curr)
            neg = min(curr,pos * curr,neg * curr)
            pos = temp_max
            
            result = max(pos,result)
            
        return result
