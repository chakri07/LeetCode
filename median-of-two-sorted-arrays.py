'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n //2
        
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
        
        l = 0 
        r = len(nums1) - 1 
        
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            a_left = nums1[i] if i >=0 else float('-inf')
            a_right = nums1[i+1] if (i+1) < len(nums1) else float('inf')
            
            b_left = nums2[j] if j >= 0 else float('-inf')
            b_right = nums2[j+1] if (j+1) < len(nums2) else float('inf')
            
            if a_left <= b_right and b_left <= a_right:
                if n %2 ==1:
                    return min(a_right,b_right)
                if n%2 ==0:
                    left = max(a_left,b_left)
                    right = min(a_right,b_right)
                    return (left+right)/2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
                