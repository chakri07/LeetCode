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

def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    ans = []
    for i in range(0, len(nums)-2):
        left = i + 1
        right = len(nums)-1
        while( left < right):
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

