'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Link https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, h: list[int]) -> int:
        l = 0
        r = len(h) - 1
        area = (r-l) * min(h[r],h[l])
        while l < r:
            if h[l] < h[r]:
                l +=1
            else:
                r = r - 1
                
            area = max(area, min(h[l],h[r]) * (r-l))
            
        return area
        