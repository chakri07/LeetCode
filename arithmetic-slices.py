'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0

Link: https://leetcode.com/problems/arithmetic-slices/
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3 : return 0 
        diff = nums[1]- nums[0]
        
        dp = [0]* len(nums)
        dp[0] = 0 
        dp[1] = 0
        if nums[2]- nums[1] == diff:
            dp[2] = 1
        result = dp[2]
        temp = result
        
        for i in range(3,len(nums)):
            if nums[i]- nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
                temp = temp + 1
                result = result + temp
        return result