class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # Sort to easily handle duplicates and allow early termination
        candidates.sort()
        
        def backtrack(index, target, curr_arr):
            # Base Case: Success
            if target == 0:
                ans.append(list(curr_arr))
                return
            
            # Explore choices
            for i in range(index, len(candidates)):
                # Skip duplicates at the same depth level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Optimization: If the current number is greater than the remaining target,
                # no point in looking further since the array is sorted.
                if candidates[i] > target:
                    break
                
                # Make choice
                curr_arr.append(candidates[i])
                
                # Move to next index (i + 1) because each number can only be used once
                backtrack(i + 1, target - candidates[i], curr_arr)
                
                # Undo choice (backtrack)
                curr_arr.pop()
        
        backtrack(0, target, [])
        return ans