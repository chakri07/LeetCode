class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starting_set = set()

        for num in num_set:
            if num -1  not in num_set:
                starting_set.add(num)

        ans = 0
        for start in starting_set:
            lenght = 1
            curr = start
            while curr + 1 in num_set:
                lenght += 1
                curr += 1

            ans = max(ans, lenght)
        
        return ans
