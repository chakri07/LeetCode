"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mark all negetive number to zero
        for i in range(0, len(nums)):
            if nums[i] < 0:
                nums[i] = 0
    """    
     itearate the array then 
     take the value in the array and mark the value at that array as -ve
     edge case:
     if number is zero mark the number as len + 1 
    """
        for i in range(len(nums)):
            val = abs(nums[i]) -1
            # print(nums)
            if 0 <= val < len(nums):
                if nums[val] > 0:
                    nums[val] = -1 * nums[val]
                elif nums[val] == 0:
                    nums[val] = -1 * (len(nums)+1)


        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        
        return len(nums)+1

        
