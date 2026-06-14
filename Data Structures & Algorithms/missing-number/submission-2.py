class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = [0]
        num_set = set(nums)

        for i in range(len(nums)+1):
            if not i in num_set:
                return i

        return len(nums)
        