'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

https://leetcode.com/problems/permutations/
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums[:]]
        result = []
        
        for _ in range(0,len(nums)):
            temp = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(temp)
                result.append(perm)
            nums.append(temp)
            
        return result