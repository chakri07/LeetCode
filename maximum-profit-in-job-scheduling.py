"""

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

https://leetcode.com/problems/maximum-profit-in-job-scheduling
"""

from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        """
        1. first did recursive solution -> we have 2 choices 
        2. Included DP -> dp store the max profit starting from i
        3. do bin search to find the next index.
        """

        n = len(startTime) 
        jobs = []

        for i in range(n):
            jobs.append([startTime[i],endTime[i],profit[i]])

        jobs = sorted(jobs, key = lambda x: x[0])
        
        # we do on changing stuff
        dp = {}
        """
        dp will store max profit acheivable starting from i or 
        after i ,... irrespective of we are taking or n
        """

        def bin_search(left):
            start = left
            right = n-1
            ans = left
            while left <= right:
                mid = (left + right)//2
                if jobs[mid][0] >= jobs[start][1]:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans


        def helper(i):
            """
            2 choices 
            1. take the job 
            2. Dont take the job
            """
            
            if i >= n:
                return 0
                
            if i in dp:
                return dp[i]
            
            
            # Dont take the job 

            profit_if_skipped = helper(i+1)

            # option 2 : take the current_job 
            curr_start_time, curr_end_time, curr_profit = jobs[i]
            
            next_idx = bin_search(i)
            # here we can do bin search

            profit_if_taken = curr_profit
            if next_idx > i:
                profit_if_taken += helper(next_idx)

            dp[i] = max(profit_if_taken, profit_if_skipped)

            return dp[i]

        helper(0)

        return max(dp.values())
