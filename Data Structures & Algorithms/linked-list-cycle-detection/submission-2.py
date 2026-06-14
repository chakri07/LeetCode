# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        if not head.next:
            return False

        slow = head 
        fast = head.next 

        while (slow and fast):
            if slow == fast:
                return True 
            
            if slow.next:
                slow = slow.next 
            else:
                return False

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False

        return False
        