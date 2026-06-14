class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 1 
        dp = [1] * len(nums)
        dp[0] = 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # that means we can add one more to the LIS at J
                    dp[i] = max(dp[i],dp[j]+1)
                    ans = max(dp[i],ans)

        return ans