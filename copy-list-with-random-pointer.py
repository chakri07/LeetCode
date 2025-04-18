'''

    A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.


https://leetcode.com/problems/copy-list-with-random-pointer/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        node_map = {}
        ref = head

        while head:
            if not head in node_map:
                node_map[head] = Node(head.val)
            
            new_head = node_map[head]
                

            nxt_node = head.next
            if nxt_node:
                if not  nxt_node in node_map:
                    new_next = Node(head.next.val)
                    node_map[nxt_node] = new_next

                new_head.next = node_map[nxt_node]

            
            rand_node = head.random
            if rand_node:
                if not rand_node in node_map:
                    new_rand = Node(rand_node.val)
                    node_map[rand_node] = new_rand
                
                new_head.random = node_map[rand_node]
            
            head = head.next

        return node_map[ref]


from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copyHead = Node(head.val)
        
        curr = head
        copyCurr = copyHead
        
        rand_map = {}
        rand_map[head] = copyHead
        
        while(curr.next):
            copyCurr.next = Node(curr.next.val)
            curr = curr.next
            copyCurr= copyCurr.next
            rand_map[curr] = copyCurr
            
        curr = head
        copyCurr = copyHead
        
        while(curr):
            if curr.random:
                copyCurr.random = rand_map[curr.random]
            copyCurr = copyCurr.next
            curr = curr.next
        
        return copyHead
        