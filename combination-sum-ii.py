'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]


Link:https://leetcode.com/problems/combination-sum-ii/
'''


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        output = []
        self.helper(0,[],0,output,candidates,target)
        return output
    
    def helper(self,pos,curr,curr_sum,output,nums,target):
        if len(curr) > len(nums):
            return
        if curr_sum == target:
            curr = sorted(curr)
            if curr not in output:
                output.append(curr[:])
        elif curr_sum > target:
            return 
        else: 
            for i in range(pos,len(nums)):
                # print(curr)
                curr.append(nums[i])
                curr_sum = curr_sum + nums[i]
                self.helper(i+1,curr,curr_sum,output,nums,target)
                curr_sum = curr_sum - curr.pop()
            
        