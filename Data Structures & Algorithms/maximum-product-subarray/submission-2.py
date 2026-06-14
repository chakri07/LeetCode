class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            temp_pos = max(nums[i], neg * nums[i], pos * nums[i])
            neg = min(nums[i], neg * nums[i], pos * nums[i])
            pos = temp_pos

            ans = max(ans, pos, neg)

        return ans