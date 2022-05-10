'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

link: https://leetcode.com/problems/subarray-product-less-than-k/
'''
#  sliding window solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1 : return 0 
        prod = 1 
        ans = 0 
        left = 0 
        for right,val in enumerate(nums):
            prod = prod * val 
            while prod >= k :
                prod = prod / nums[left]
                left = left + 1
            ans = ans + right -left + 1
            
        return ans