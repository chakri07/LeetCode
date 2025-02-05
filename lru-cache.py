'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

https://leetcode.com/problems/lru-cache/
'''

class Node:
    def __init__(self,key,val):
        # double linked list
        self.key ,self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right , self.left
        
        
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev
        
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next , node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

## Similar implementation

class Node:
    def __init__(self,key=0,value=0):
        self.key,self.value = key,value
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            curr_node = self.map[key]

            before,after = curr_node.prev, curr_node.next

            before.next = after
            after.prev = before

            self.__insertAtHead__(curr_node)
            return self.map[key].value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.map[key].value = value
            curr_node = self.map[key]

            before,after = curr_node.prev, curr_node.next

            before.next = after
            after.prev = before

            curr_node.next,curr_node.prev = None,None
            self.__insertAtHead__(curr_node)
            return

        newNode = Node(key,value)
        if len(self.map) >= self.capacity:
            self.__removeAtTail__()

        self.__insertAtHead__(newNode)
        self.map[key] = newNode

        
    def __removeAtTail__(self):
        remove_node = self.tail.prev
        pen_ultimate = remove_node.prev

        pen_ultimate.next = self.tail
        self.tail.prev = pen_ultimate

        self.map.pop(remove_node.key)
        del remove_node

    def __insertAtHead__(self,curr_node):
        prev_first = self.head.next

        self.head.next = curr_node
        curr_node.prev = self.head

        curr_node.next = prev_first
        prev_first.prev = curr_node
