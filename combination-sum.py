'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Link:https://leetcode.com/problems/combination-sum/
'''

# most optimized
class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        def helper(path,curr_sum,index):
            curr_num = nums[index]

            path.append(curr_num)
            curr_sum += curr_num

            if curr_sum == target:
                temp = path[:]
                temp = sorted(temp)
                ans.add(tuple(temp))

            if curr_sum < target: 
                for i in range(index,len(nums)):
                    helper(path,curr_sum,i)

            path.pop()

        for i in range(len(nums)):
            helper([],0,i)

        return list(ans)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        self.helper(0,[],target,output,candidates)
        return output
    
    
    def helper(self,curr_sum,curr,target,output,nums):
        if curr_sum == target:
            curr = sorted(curr)
            if curr not in output:
                output.append(curr[:])
            
            return
        elif curr_sum > target:
            return
        else:
            for i in range(0,len(nums)):
                # print(curr)
                curr.append(nums[i])
                curr_sum = curr_sum + nums[i]
                self.helper(curr_sum,curr,target,output,nums)
                n = curr.pop()
                curr_sum = curr_sum - n 

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def helper(candidates, target,till,ans):
            s = sum(till)
            if s == target:
                output = till[:]
                output.sort()
                if  output not in ans:
                    ans.append(output)
                return
            if s > target:
                return 
            if s < target:
                for num in candidates:
                    till.append(num)
                    helper(candidates,target,till,ans)
                    till.pop()
                    
        ans = []
        helper(candidates,target,[],ans)
            
        return ans
                    