"""
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

 

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 108
 

Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?



https://leetcode.com/problems/missing-element-in-sorted-array
"""


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:  # Changed the loop condition
            mid = (right + left) // 2

            missing_count = (nums[mid] - nums[0]) - mid

            if missing_count < k:
                left = mid + 1  # Move left pointer past mid
            else:
                right = mid - 1 # Move right pointer before mid

        # After the loop, 'left' points to the index where the k-th missing number
        # would be inserted if the array were complete.
        # The number of missing elements before index 'left' is (nums[left-1] - nums[0]) - (left - 1)
        # if left > 0, otherwise it's 0.


        missing_before_left = (nums[left - 1] - nums[0] - (left - 1)) if left > 0 else 0

        return nums[left - 1] + (k - missing_before_left) if left > 0 else nums[0] + k