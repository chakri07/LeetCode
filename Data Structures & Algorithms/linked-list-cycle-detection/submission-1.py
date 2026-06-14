# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        slow = head
        fast = head.next.next

        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
        
        return False
        
             
