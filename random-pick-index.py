"""
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.

https://leetcode.com/problems/random-pick-index
"""
# using binary search
import random
class Solution:

    def __init__(self, w: List[int]):
        self.sum_arr = []
        self.prefix_sum = 0 
        
        for i in range(len(w)):
            self.prefix_sum += w[i]
            self.sum_arr.append(self.prefix_sum)

    def pickIndex(self) -> int:


        target = random.randint(1, self.prefix_sum)
        
        low, high = 0, len(self.sum_arr)-1 
        while low <= high:
            mid = (low + high)//2

            if target == self.sum_arr[mid]:
                return mid

            if target > self.sum_arr[mid]:
                low = mid + 1
            else:
                high = mid -1

        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.idx_map = defaultdict(list)

        for i in range(len(nums)):
            self.idx_map[nums[i]].append(i)


    def pick(self, target: int) -> int:
        rand = random.randint(0,len(self.idx_map[target])-1)
        return self.idx_map[target][rand]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)