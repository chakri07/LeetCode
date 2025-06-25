"""

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.


https://leetcode.com/problems/longest-mountain-in-array
"""
from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3: # A mountain must have at least 3 elements
            return 0

        max_len = 0
        base = 0

        while base < n:
            end = base
            
            if end + 1 < n and arr[end] < arr[end+1]:
                while end + 1 < n and arr[end] < arr[end+1]:
                    end += 1
            else:
                base += 1
                continue 

            peak = end

            if end + 1 < n and arr[end] > arr[end+1]: 
                while end + 1 < n and arr[end] > arr[end+1]:
                    end += 1
            else:
                base = peak + 1 
                continue 
            

            current_mountain_len = end - base + 1
            max_len = max(max_len, current_mountain_len)

            base = end

        return max_len
