"""

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets

https://leetcode.com/problems/partition-equal-subset-sum/description/

"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums) % 2 == 1:
            return False
        
        # check if there is a subset of sum exactly half 
        target = sum(nums)//2
        dp = [False] * (target+1)
        dp[0] = True
        # dp[i] indicates whether a sum i can be formed using the elements.
        
        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        return dp[target]
            
