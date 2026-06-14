class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(curr,curr_sum):
            if curr_sum == target:
                curr = sorted(curr)
                if curr not in ans:
                    ans.append(curr[:])

            elif curr_sum > target:
                return 
            else: 
                for num in nums:
                    curr.append(num)
                    curr_sum = curr_sum + num
                    helper(curr,curr_sum)

                    n = curr.pop()
                    curr_sum = curr_sum - n
                    
        ans = []
        helper([],0)
        return ans