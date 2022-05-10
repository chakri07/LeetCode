'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



https://leetcode.com/problems/trapping-rain-water
'''

class Solution:
    def trap(self, h: list[int]) -> int:
        left = [0] * len(h)
        right = [0] * len(h)
        
        left[0] = h[0]
        right[-1] = h[-1]
        
        maxl = left[0]
        maxr = right[-1]
        
        for i in range(0,len(h)):
            if h[i]> maxl:
                maxl = h[i]
            left[i] = maxl
            
        for i in range(len(h)-1,-1,-1):
            if h[i] > maxr:
                maxr = h[i]
            right[i] = maxr
            
        ans = 0 
        for i in range(0,len(h)):
            ans = ans + (min(left[i],right[i])-h[i])
            
        return ans