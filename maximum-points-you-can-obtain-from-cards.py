'''
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''

from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        front_score = [0] * (k+1)
        back_score = [0] * (k+1)
        n = len(cardPoints)

        for i in range(k):
            front_score[i+1]  = front_score[i] + cardPoints[i]    
        
        for i in range(k):
            back_score[i+1] = back_score[i] + cardPoints[n-i-1]

        max_score = 0

        for i in range(k+1):
            curr_score = front_score[i] + back_score[k-i]
            max_score = max(max_score, curr_score)

        return max_score



#  sliding window solution its really good
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # Time Complexity: O(k)
        # Space Complexity: O(1)
        
        window_start = 0
        max_points = 0
        
        for i in range(len(cardPoints) - k, len(cardPoints)):
            max_points += cardPoints[i]
            
        running_points = max_points
        
        for window_end in range(len(cardPoints) - k, len(cardPoints)):
            running_points += cardPoints[window_start] - cardPoints[window_end]
            max_points = max(running_points, max_points)
            window_start += 1
            
        return max_points