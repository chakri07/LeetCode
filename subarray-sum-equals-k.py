"""


Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):

        prefix_sum = 0

        count_map = defaultdict(int)

        ans = 0 

        for num in nums:
            prefix_sum += num

            if prefix_sum == k:
                ans += 1
            
            if prefix_sum -k in count_map:
                ans += count_map[prefix_sum-k]

            count_map[prefix_sum] += 1
        
        return ans



class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count_map = {0: 1}  # Stores frequency of prefix sums
        count = 0

        for num in nums:
            prefix_sum += num
            
            # If (prefix_sum - k) exists in map, add its count to result
            if prefix_sum - k in count_map:
                count += count_map[prefix_sum - k]
            
            # Store the current prefix sum in map
            count_map[prefix_sum] = count_map.get(prefix_sum, 0) + 1

        return count
