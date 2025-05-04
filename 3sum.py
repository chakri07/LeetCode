'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

link : https://leetcode.com/problems/3sum/
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
                continue
            left = i+1 
            right = len(nums)-1

            while left < right:
                s = nums[i] + nums[left]+ nums[right]
                if s == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1 
                    right -= 1 
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left +=1 
        
        return ans



def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    ans = []
    for i in range(0, len(nums)-2):
        left = i + 1
        right = len(nums)-1
        while( left < right ):
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0 :
                sortedArray = sorted([nums[i],nums[left],nums[right]])
                if sortedArray not in ans:
                    ans.append(sortedArray)
                left = left +1 
            elif sum > 0 : 
                right = right - 1
            else :
                left = left + 1
    return ans

