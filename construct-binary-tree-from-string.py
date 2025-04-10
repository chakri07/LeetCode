"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]

https://leetcode.com/problems/construct-binary-tree-from-string/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _getNumber(self,s,idx):
        is_neg = False
        if s[idx] == '-':
            is_neg = True
            idx += 1
        
        number = ''
        while idx < len(s) and s[idx].isdigit():
            number += s[idx]
            idx +=1
        
        return int(number) if not is_neg else -1 * int(number), idx
    
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        root = TreeNode()
        stack = [root]

        idx = 0 

        while idx < len(s):
            node = stack.pop()

            # not started conditio 
            if s[idx] == '-' or s[idx].isdigit():
                value,idx  = self._getNumber(s,idx)
                node.val = value
            
                if idx < len(s) and s[idx] == '(':
                    stack.append(node)

                    node.left = TreeNode()
                    stack.append(node.left)

            # Left done
            elif node.left and s[idx] == '(':
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)

            idx += 1
        return stack.pop() if stack else root