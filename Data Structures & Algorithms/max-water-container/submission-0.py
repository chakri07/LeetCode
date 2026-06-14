class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        left = 0 
        right = len(heights) -1 

        while left < right: 
            area = min(heights[right],heights[left]) * (right-left)

            if area > max_area: 
                max_area = area
            if heights[right] < heights[left]:
                right -=1 
            else:
                left +=1 
        
        return max_area
        