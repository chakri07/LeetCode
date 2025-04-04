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

if head.next == None and n ==1:
            return None
        temp = head
        length = 0 

        while temp:
            length += 1
            temp = temp.next

        if n == length:
            return head.next

        count = 1
        temp = head
        while count <  length - n:
            temp = temp.next
            count += 1

        remove_node = temp.next
        
        temp.next = remove_node.next

        return head