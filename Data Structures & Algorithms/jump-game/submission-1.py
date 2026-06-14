class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[-1] = True

        for i in range(n-2,-1,-1):
            max_jump = nums[i]
            for j in range(i+1, min(i+max_jump+1, n)):
                if dp[j]:
                    dp[i] = True

        return dp[0]