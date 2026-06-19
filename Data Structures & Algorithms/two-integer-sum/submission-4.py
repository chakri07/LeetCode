class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for idx, num in enumerate(nums):
            reminder = target - num
            if reminder in seen_map:
                return [seen_map[reminder], idx]
            
            seen_map[num] = idx