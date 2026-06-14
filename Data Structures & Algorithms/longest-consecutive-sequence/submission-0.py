class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0 

        for num in nums:
            if num-1 not in num_set:
                lenght = 1
                while num + lenght in num_set:
                    lenght += 1
                ans = max(ans, lenght)
        
        return ans
                
