'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n ==0:
            return head
        if head.next == None and n ==1:
            return None
        ln = 0 
        temp = head
        while(temp):
            temp = temp.next
            ln+=1
        if n == ln:
            return head.next
        
        temp = head
        for i in range(0,ln-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head