'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0



Link: https://leetcode.com/problems/minimum-size-subarray-sum/
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if len(nums) == 0 :
            return 0 
        if len(nums) ==1 : 
            if nums[0] == target:
                return 1
            else:
                return 0 
        sum = 0 
        left = 0 
        ans = len(nums)
        flag = False
        for right,val in enumerate(nums):
            sum = sum + val
            while sum >= target:
                sum = sum - nums[left]
                if ans >= (right-left+1):
                    flag = True
                    ans = right - left +1 
                left = left + 1   
        if flag: 
            return ans
        else : 
            return 0 
            