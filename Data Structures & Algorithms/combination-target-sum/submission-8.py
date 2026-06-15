class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        self.helper(0,nums,target,[],output)

        return output

    def helper(self,idx,nums,target,curr,output):
        if target == 0:
            output.append(curr[:])
            return

        if target < 0 or idx >= len(nums):
            return 
        
        for i in range(idx, len(nums)):
            curr.append(nums[i])
            self.helper(i, nums, target - nums[i], curr,output)
            curr.pop()

            
    

        