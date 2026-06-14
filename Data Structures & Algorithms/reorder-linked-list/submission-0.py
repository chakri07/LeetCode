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

        