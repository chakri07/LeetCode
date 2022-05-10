"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(-1,head)
        
        prev,curr = ans,head
        
        while(curr and curr.next):
            second = curr.next
            nextPair = second.next 

            # Swap the nodes 
            second.next = curr    # relocate second node to first pos
            curr.next = nextPair  # connect curr pair to next pair
            prev.next = second   # link prev node to swapped Pair
            
            prev, curr = curr, nextPair
            
            
        return ans.next