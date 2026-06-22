class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)

        for i in range(1,len(nums)):
            left_arr[i] = nums[i-1] * left_arr[i-1]

        for i in range(len(nums)-2,-1,-1):
            right_arr[i] = nums[i+1] * right_arr[i+1]

        result = []
        for i in range(0,len(nums)):
            result.append(left_arr[i] * right_arr[i])

        return result
            


        
            
