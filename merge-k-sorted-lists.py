'''

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104

https://leetcode.com/problems/merge-k-sorted-lists/
'''
# divide and conquer by popping lists from first and last
# instead of using lists next to each other. 
# same complexity as we are reducing half computation 
# easier to code.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # lets do divide and conquer
        # so each time the list and the next one to it is merged

        def mergeTwoLists(l1,l2):
            head = ListNode()
            ans = head 
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                
                head = head.next

            if l1:
                head.next = l1
            if l2:
                head.next = l2

            return ans.next
        
        # instead of doing one next to each other we can like
        # 1st and last, 2nd and last 2nd etc ...

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            # print(lists)
            remaining = len(lists)
            temp = []
            for i in range(0,remaining//2):
                l1 = lists.pop(0)
                l2 = lists.pop()
                merged = mergeTwoLists(l1,l2)
                temp.append(merged)
            
            lists.extend(temp)
            

        return lists[0] 

# simpler heap using just nide directly instead of index and stuff to make it
# complicated 

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []

        head = ListNode()
        ans = head

        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,node))

        while heap:
            _,curr_node = heapq.heappop(heap)

            head.next = curr_node
            head = head.next

            if curr_node.next:
                heapq.heappush(heap,(curr_node.next.val,curr_node.next))

        return ans.next


## Merging two lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

        for l in lists:
            ans_head = merge_two(ans_head,l)
            

        return ans_head.next
                    

## Heap
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        ans = ListNode()
        curr = ans
        heapq.heapify(min_heap)
        
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(min_heap,(l.val,i))
                
        while(min_heap):
            val,i = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap,(lists[i].val,i))
                
        return ans.next
            