class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(nums[idx]+dp[idx-2], dp[idx-1])

        return dp[-1]

