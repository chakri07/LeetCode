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
        n = len(startTime)
        jobs = []
        
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))

        jobs = sorted(jobs, key = lambda x : x[0])

        dp= {}

        # dp represent max profit you can get starting from job i

        def binarySearch(curr):
            left = curr + 1
            right = n - 1

            if left >= n:
                return -1
            ans = -1
            while left <= right:
                mid = (left + right)//2
                if jobs[mid][0] >= jobs[curr][1]:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        def helper(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            #choice 1 : job is taken
            next_idx = -1

            # # this can be binary search
            # for j in range(i,n):
            #     if jobs[j][0] >= jobs[i][1]:
            #         next_idx = j
            #         break
            
            next_idx = binarySearch(i)

            profit_if_taken = jobs[i][2]
            if next_idx != -1:
                profit_if_taken += helper(next_idx)

            # choice 2: job not taken
            profit_not_taken = helper(i+1)

            dp[i] = max(profit_not_taken, profit_if_taken)

            return dp[i]

        helper(0)


        return max(dp.values())