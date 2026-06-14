from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Return 1-based indices as required by the problem
                return [left + 1, right + 1]
            elif current_sum < target:
                # Need a larger sum, move left pointer to increase value
                left += 1
            else: # current_sum > target
                # Need a smaller sum, move right pointer to decrease value
                right -= 1
        
        # This part should ideally not be reached if a solution is guaranteed
        return []