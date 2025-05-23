"""

31. Next Permutation
Medium
Topics
Companies
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

https://leetcode.com/problems/next-permutation/description/
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1 : Find the first number that is decreasing from right 
        # step 2 : Find a number greater than that number and swap 
        # step 3 : then reverse everything thats after that 

        decreasing_idx = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                decreasing_idx = i
                break
        
        if decreasing_idx == -1:
            nums.reverse()
            return 
        # find the next greate number 

        for i in range(len(nums)-1, decreasing_idx, -1):
            if nums[i] > nums[decreasing_idx]:
                nums[i], nums[decreasing_idx] = nums[decreasing_idx], nums[i]
                break
        
        # then reversed the part after decreasing_idx
        left = decreasing_idx + 1
        right = len(nums) - 1  

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1





class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an element is found, find the next larger element and swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap
        
        # Step 3: Reverse the elements after index i
        nums[i + 1:] = reversed(nums[i + 1:])
        