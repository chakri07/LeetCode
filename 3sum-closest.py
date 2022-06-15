'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104

https://leetcode.com/problems/3sum-closest/
'''

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        maxDiff = float('inf')
        ans = 0 
        nums.sort()
        for idx in range(0, len(nums)-2):
            curr = nums[idx]
            left = idx+1
            right = len(nums) -1
            while(left < right):
                curr_sum = nums[left]+ nums[right] + curr
                diff = abs(curr_sum - target)
                if diff < maxDiff:
                    ans = curr_sum
                    maxDiff = diff
                if curr_sum > target:
                    right = right - 1
                elif curr_sum < target:
                    left = left + 1 
                else:
                    return target
                
                    
        return ans
         