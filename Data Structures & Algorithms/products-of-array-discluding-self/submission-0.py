class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        before = []
        after = []
        for index in range(len(nums)):
            after.append(1)

        for index, val in enumerate(nums):
            if index == 0 : 
                before.append(1)
            else : 
                before.append(before[index-1] * nums[index-1])
        
        for index in range(len(nums)-1,-1,-1): 
            if index == len(nums) - 1: 
                after[index] = 1
            else : 
                after[index] = (after[index+1] * nums[index+1])

        output = []
        for i in range(len(nums)): 
            output.append(after[i] * before[i])

        return output