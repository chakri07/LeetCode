"""

You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].

Return the maximum possible length of a good subsequence of nums.

 

Example 1:

Input: nums = [1,2,1,1,3], k = 2

Output: 4

Explanation:

The maximum length subsequence is [1,2,1,1,3].

Example 2:

Input: nums = [1,2,3,4,5,1], k = 0

Output: 2

Explanation:


https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i
"""
from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, A: List[int], k: int) -> int:

        dp = [defaultdict(int) for i in range(k + 1)]

        res = [0] * (k + 1)
        
        for a in A:
            for i in range(k, -1, -1):
                # if i == a just increase in length with no increase in num pairs
                # if i! == a we do 1 + max Number of paris so we use result to track that,
                dp[i][a] = max(dp[i][a] + 1, res[i - 1] + 1 if i != 0 else 0)
                res[i] = max(res[i], dp[i][a])
        return res[k]