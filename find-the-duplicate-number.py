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

# Tortise and hare algorithm.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # phase 1 find a meeting point
        slow, fast= nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # phase 2 reset the slow to start and move until slow and fast meet and 
        # move both of them one step each 
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# modifying nums solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):  # Iterate through the list
            curr_val = abs(nums[i])    # Get the absolute value of the current element
            if nums[curr_val - 1] < 0:  # Check if the value at index (curr_val - 1) is negative
                return curr_val         # If negative, it means we have already visited this number, so return it
            nums[curr_val - 1] *= -1    # Mark the index (curr_val - 1) as visited by making it negative
