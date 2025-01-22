"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]

https://neetcode.io/problems/reorder-linked-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None # Cutting of the lists

        def reverse(node):
            curr = node
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev

                prev = curr
                curr = nxt

            pr = prev
            while pr:
                print(pr.val)
                pr = pr.next

            return prev

        p2 = reverse(mid)
        p1 = head

        while p1 and p2: 
            t1,t2 = p1.next, p2.next

            p1.next = p2
            p2.next = t1

            p1,p2 = t1,t2

        