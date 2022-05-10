'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Link: https://leetcode.com/problems/permutations-ii
'''

# back trackking

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        if len(nums) == 1: 
            return [nums[:]]
        for _ in range(0,len(nums)):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
            for perm in perms:
                if perm not in result:
                    result.append(perm)
            nums.append(n)
        return result