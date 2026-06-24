class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] 
        curr_sum = nums[0] 
        
        for num in nums[1:]:
            if curr_sum < 0:
                # ignore and restart
                curr_sum = num
            else:
                curr_sum += num
                max_sum = max(max_sum, curr_sum)


        return max(max_sum,curr_sum)

            
        