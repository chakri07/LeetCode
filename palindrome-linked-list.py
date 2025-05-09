"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9



https://leetcode.com/problems/palindrome-linked-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(head):
            prev, curr = None, head

            while curr: 
                nex = curr.next

                curr.next = prev 

                prev = curr
                curr = nex
            
            return prev
        
        # we can do the tortise and hare algo 
        if not head:
            return True
        
        slow = head 
        fast = head.next 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # slow will the mid pointer 
        temp = slow.next 
        slow.next = None
        other_half = reverse(temp)

        while head and other_half:
            if head.val != other_half.val:
                return False
                
            head = head.next 
            other_half = other_half.next

        return True
