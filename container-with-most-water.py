'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Link https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0 
        left = 0 
        right = len(height)-1
        while( left < right):
            area = self.getArea(left,height[left],right, height[right])
            max_area = max(area, max_area)
            if height[left]< height[right]:
                left = left + 1
            else : 
                right = right -1                   
        return max_area
     
    
    
    def getArea(self,x1: int , y1: int, x2 :int, y2:int) -> int:
        length = abs(x1-x2)
        if y1 < y2:
            return length * y1
        else:
            return length * y2
        