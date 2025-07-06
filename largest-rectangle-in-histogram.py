"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 


https://leetcode.com/problems/largest-rectangle-in-histogram
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                width = i - stack[-1] - 1
                
                max_area = max(max_area, current_height * width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)

        return max_area


from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helper(start,end):
            if start > end:
                return 0 
            
            min_idx = start
            for i in range(start, end+1):
                if heights[i] < heights[min_idx]:
                    min_idx = i
            
            return max(
                heights[min_idx] * (end-start+1),
                helper(start,min_idx-1),
                helper(min_idx+1,end),
            )

        return helper(0, len(heights)-1)