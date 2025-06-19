"""

Mario drives on a two-lane freeway with coins every mile. You are given two integer arrays, lane1 and lane2, where the value at the ith index represents the number of coins he gains or loses in the ith mile in that lane.

If Mario is in lane 1 at mile i and lane1[i] > 0, Mario gains lane1[i] coins.
If Mario is in lane 1 at mile i and lane1[i] < 0, Mario pays a toll and loses abs(lane1[i]) coins.
The same rules apply for lane2.
Mario can enter the freeway anywhere and exit anytime after traveling at least one mile. Mario always enters the freeway on lane 1 but can switch lanes at most 2 times.

A lane switch is when Mario goes from lane 1 to lane 2 or vice versa.

Return the maximum number of coins Mario can earn after performing at most 2 lane switches.

Note: Mario can switch lanes immediately upon entering or just before exiting the freeway.

 

Example 1:

Input: lane1 = [1,-2,-10,3], lane2 = [-5,10,0,1]

Output: 14

Explanation:

Mario drives the first mile on lane 1.
He then changes to lane 2 and drives for two miles.
He changes back to lane 1 for the last mile.
Mario collects 1 + 10 + 0 + 3 = 14 coins.

Example 2:

Input: lane1 = [1,-1,-1,-1], lane2 = [0,3,4,-5]

Output: 8

Explanation:

Mario starts at mile 0 in lane 1 and drives one mile.
He then changes to lane 2 and drives for two more miles. He exits the freeway before mile 3.
He collects 1 + 3 + 4 = 8 coins.

Example 3:

Input: lane1 = [-5,-4,-3], lane2 = [-1,2,3]

Output: 5

Explanation:

Mario enters at mile 1 and immediately switches to lane 2. He stays here the entire way.
He collects a total of 2 + 3 = 5 coins.

Example 4:

Input: lane1 = [-3,-3,-3], lane2 = [9,-2,4]

Output: 11

Explanation:

Mario starts at the beginning of the freeway and immediately switches to lane 2. He stays here the whole way.
He collects a total of 9 + (-2) + 4 = 11 coins.

Example 5:

Input: lane1 = [-10], lane2 = [-2]

Output: -2

Explanation:

Since Mario must ride on the freeway for at least one mile, he rides just one mile in lane 2.
He collects a total of -2 coins.

https://leetcode.com/problems/maximum-coin-collection
"""

import math

class Solution:
    def maxCoins(self, lane1: list[int], lane2: list[int]) -> int:
        n = len(lane1)

        # dp_lane1_0: max coins ending in lane 1 with 0 switches
        # dp_lane2_1: max coins ending in lane 2 with 1 switch
        # dp_lane1_2: max coins ending in lane 1 with 2 switches
        
        # Initialize with negative infinity to represent no valid path yet.
        # This handles cases where all coin values might be negative.
        dp_lane1_0 = float('-inf')
        dp_lane2_1 = float('-inf')
        dp_lane1_2 = float('-inf')

        max_overall_coins = float('-inf')

        for i in range(n):
            # Calculate current_dp values for mile 'i' based on previous mile's dp values
            # and by potentially starting a new path at mile 'i'.

            # For lane1_0 (ending in lane 1, 0 switches):
            # Option 1: Start a new path at mile 'i' in lane 1.
            # Option 2: Continue from the previous mile in lane 1 with 0 switches.
            current_lane1_0 = lane1[i]
            # entering at lane1 with no switches done.
            if dp_lane1_0 != float('-inf'):
                current_lane1_0 = max(current_lane1_0, dp_lane1_0 + lane1[i])
            
            # For lane2_1 (ending in lane 2, 1 switch):
            # Option 1: Start a new path at mile 'i', immediately switch from lane 1 to lane 2.
            # Option 2: Continue from the previous mile in lane 2 with 1 switch.
            # Option 3: Switch from lane 1 (0 switches) at previous mile to lane 2 at current mile (uses 1st switch).
            current_lane2_1 = lane2[i] # Starting fresh at i, but in lane 2 means 1 switch from L1
            if dp_lane2_1 != float('-inf'):
                current_lane2_1 = max(current_lane2_1, dp_lane2_1 + lane2[i])
            if dp_lane1_0 != float('-inf'):
                current_lane2_1 = max(current_lane2_1, dp_lane1_0 + lane2[i])

            # For lane1_2 (ending in lane 1, 2 switches):
            # Option 1: Start a new path at mile 'i', immediately switch L1->L2->L1.
            # Option 2: Continue from the previous mile in lane 1 with 2 switches.
            # Option 3: Switch from lane 2 (1 switch) at previous mile to lane 1 at current mile (uses 2nd switch).
            current_lane1_2 = lane1[i] # Starting fresh at i, but in lane 1 after 2 switches
            if dp_lane1_2 != float('-inf'):
                current_lane1_2 = max(current_lane1_2, dp_lane1_2 + lane1[i])
            if dp_lane2_1 != float('-inf'):
                current_lane1_2 = max(current_lane1_2, dp_lane2_1 + lane1[i])

            # Update the dp values for the next iteration
            dp_lane1_0 = current_lane1_0
            dp_lane2_1 = current_lane2_1
            dp_lane1_2 = current_lane1_2

            # Update the overall maximum coins earned
            max_overall_coins = max(max_overall_coins, dp_lane1_0, dp_lane2_1, dp_lane1_2)

        return max_overall_coins