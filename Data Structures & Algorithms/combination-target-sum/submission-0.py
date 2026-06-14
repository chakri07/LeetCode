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