'''

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

https://leetcode.com/problems/reverse-nodes-in-k-group
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        
        next_head = tail
        ret_head,ret_tail = self.reverseOnegroup(head,tail)
        ret_tail.next = self.reverseKGroup(next_head,k)
        
        return ret_head
        
    def reverseOnegroup(self,head, tail):
        
        curr = head
        prev = None
        while(curr != tail):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        reverse_head = prev
        while prev.next:
            prev = prev.next
        reverse_tail = prev
        
        return reverse_head,reverse_tail
            
        