class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_max = [0] * n
        left_max = []


        # first lets populate left dp
        left_till = 0
        for i in range(n):
            left_till = max(left_till, height[i])
            left_max.append(left_till)

        right_till = 0 
        for i in range(len(height)-1,-1,-1):
            right_till = max(right_till,  height[i])
            right_max[i] = right_till

        ans = 0
        for i in range(1,n):
            ans += max(0, min(right_max[i], left_max[i]) - height[i])

        return ans

