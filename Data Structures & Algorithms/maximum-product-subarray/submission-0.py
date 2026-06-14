class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        pos,neg = nums[0],nums[0]
        result = nums[0]
        
        for curr in nums[1:]:

            tmp_max = max(curr, pos * curr, neg*curr)
            neg = min(curr, pos * curr, neg*curr)
            pos = tmp_max

            result = max(result, pos)

        return result