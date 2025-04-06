"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105


https://leetcode.com/problems/contains-duplicate-ii
"""
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        num_map = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]
            if num in num_map:
                prev = num_map[num]
                if abs(i-prev) <= k:
                        return True

            num_map[num] = i
        return False
