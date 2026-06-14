class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(curr,curr_sum):
            if curr_sum == target:
                sort_ans = sorted(curr)
                if sort_ans not in ans:
                    ans.append(sort_ans)
            elif curr_sum > target:
                return 
            else:
                for num in nums: 
                    curr.append(num)
                    curr_sum = curr_sum + num
                    helper(curr,curr_sum)
                    n = curr.pop()
                    curr_sum = curr_sum - n 
        
        helper([],0)

        return ans