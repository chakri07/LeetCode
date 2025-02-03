"""
78. Subsets
Medium
Topics
Companies
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

https://leetcode.com/problems/subsets/description/
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def dfs(count,curr):
            if count >= len(nums):
                results.append(curr[:])
                return
            
            
            # include the number
            curr.append(nums[count])
            dfs(count+1, curr)
            # don't include the number
            curr.pop()
            dfs(count+1, curr)
        
        dfs(0,[])
        return results



