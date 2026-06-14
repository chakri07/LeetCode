# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(l1,l2):
            ans_head = ListNode()
            tail = ans_head
            while l1 and l2:
                if l1.val < l2.val:
                    ans_head.next = l1
                    l1 = l1.next
                else:
                    ans_head.next = l2
                    l2 = l2.next
                ans_head = ans_head.next
            
            if l1:
                ans_head.next = l1
            if l2:
                ans_head.next = l2

            return tail.next

        ans_head = ListNode(float('-inf'))
        final = ans_head

        for l in lists:
            ans_head = merge_two(ans_head,l)
            

        return ans_head.next
                    