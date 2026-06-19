class DllNode:
    def __init__(self,key,val):
        self.nex = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DllNode(0,0)
        self.tail = DllNode(0,0)

        self.head.nex = self.tail
        self.tail.prev = self.head

        self.node_map = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1 
        
        node = self.node_map[key]
        self.removeNode(node)
        self.insertAtHead(node)

        return node.val

        
    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            # 1. If it exists, pull it out of its current position first
            node = self.node_map[key]
            self.removeNode(node)
            node.val = value
        else:
            # 2. If it's new, create it
            node = DllNode(key, value)
            self.node_map[key] = node
            
            # 3. Check capacity ONLY when adding a genuinely new node
            if len(self.node_map) > self.capacity:
                self.evictFromTail()

        # 4. Now safely place it at the head (works for both new and updated nodes)
        self.insertAtHead(node)


    def insertAtHead(self,node):
        head_node = self.head
        next_node = head_node.nex
        
        head_node.nex = node
        node.prev = head_node

        node.nex = next_node
        next_node.prev = node

    
    def removeNode(self,node):
        prev_node = node.prev
        next_node = node.nex

        prev_node.nex = next_node
        next_node.prev = prev_node

        node.nex = None 
        node.prev = None

    def evictFromTail(self):
        tail = self.tail

        end = tail.prev 
        new_end = end.prev
        
        del self.node_map[end.key]

        new_end.nex = tail 
        tail.prev = new_end

        




