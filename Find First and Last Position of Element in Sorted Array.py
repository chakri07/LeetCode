'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

def searchRange(self, nums: list[int], target: int) -> list[int]:
    lb =-1
    ub = -1
    start= 0
    r = len(nums)-1
    
    while( start <=r):
        mid  =start+(r-start)//2
        if nums[mid] == target:
            lb = mid
            r = mid -1 
        elif nums[mid]> target:
            r = mid
        else :
            start = mid +1
    
    start =0
    r = len(nums)-1
    while( start<=r):
        mid=start+(r-start)//2
        if nums[mid] == target:
            ub = mid
            start = mid + 1 
        elif nums[mid] >target:
            r = mid
        else :
            start = mid +1       
    return [lb,ub]