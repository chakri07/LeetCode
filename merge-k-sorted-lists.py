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
            