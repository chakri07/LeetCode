'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Link : https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0,None)
        head = ans
        n1 = 0 
        n2 = 0 
        carry = 0 
        while(l1 or l2):
            if not l1:
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next
            if not l2:
                n2 = 0 
            else:
                n2 = l2.val
                l2 = l2.next
            val = (carry+ n1+n2)%10
            carry = (carry+ n1+n2)//10
            ans.next = ListNode(val,None)
            ans = ans.next
            
        if carry !=0: 
            ans.next = ListNode(carry,None)

        return head.next

