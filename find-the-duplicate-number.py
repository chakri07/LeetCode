'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.



https://leetcode.com/problems/find-the-duplicate-number/
'''

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            curr_val = abs(nums[i])
            if nums[curr_val -1 ] <0 :
                return curr_val
            nums[curr_val -1 ] = -1 * nums[curr_val -1 ]