class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum +=num
            max_sum = max(max_sum,curr_sum)

        return max_sum

        




