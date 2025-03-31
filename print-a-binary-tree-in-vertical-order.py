"""
Given a root of a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, N, N, N, 8, N, 9]
     Vertical-Taversal-          
Output: [[4], [2], [1, 5, 6], [3, 8], [7], [9]]
Explanation: The below image shows the horizontal distances used to print vertical traversal starting from the leftmost level to the rightmost level.
     
Input: root[] = [1, 2, 3, 4, 5, N, 6]
     
Output: [[4], [2], [1, 5], [3], [6]]
Explanation: From left to right the vertical order will be [[4], [2], [1, 5], [3], [6]]
Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 105

https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
"""

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import defaultdict
class Solution:
    
    def verticalOrder(self, root):
        ans = defaultdict(list)
        
        min_col = [float('inf')]
        max_col = [float('-inf')]
        
        def dfs(node,col):
            if not node:
                return
            
            ans[col].append(node.data)
            min_col[0] = min(col,min_col[0])
            max_col[0] = max(col,max_col[0])
            
            if node.left:
                dfs(node.left,col-1)
                
            if node.right:
                dfs(node.right,col+1)
            
            return 
        
        dfs(root,0)
        final_ans = []
        for i in range(min_col[0],max_col[0]+1):
            if i in ans:
                final_ans.append(ans[i])
        
            
        return final_ans
        
