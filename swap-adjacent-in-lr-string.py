'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false


link: https://leetcode.com/problems/swap-adjacent-in-lr-string/
'''

"""
1. Check if the sequence of L and R are the same.
2. Check if the index of L in the "start" are larger than index of the L in the "end", since L can only move left.
3. Check if the index of R in the "start" are smaller than index of the R in the "end", since R can only move left.
"""
class Solution(object):
    def canTransform(self, start, end):
        if len(start)!=len(end): return False
        if start.replace('X', '')!=end.replace('X', ''): return False #[1]
        
		#[2]
        startLIndex = [i for i, c in enumerate(start) if c=='L']
        endLIndex = [i for i, c in enumerate(end) if c=='L']
        for i in range(len(startLIndex)):
            if startLIndex[i]<endLIndex[i]:
                return False
        
		#[3]
        startRIndex = [i for i, c in enumerate(start) if c=='R']
        endRIndex = [i for i, c in enumerate(end) if c=='R']
        for i in range(len(startRIndex)):
            if startRIndex[i]>endRIndex[i]:
                return False
        
        return True