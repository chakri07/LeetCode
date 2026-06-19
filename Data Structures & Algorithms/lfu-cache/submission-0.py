class DllNode:
    def __init__(self, key, value):
        self.nex = None
        self.prev = None
        self.key = key 
        self.value = value 
        self.freq = 0
        

class Dll:
    def __init__(self):
        self.head = DllNode(0, 0)
        self.tail = DllNode(0, 0)
        self.head.nex = self.tail
        self.tail.prev = self.head
        self.length = 0 

    def remove(self, node):
        temp_next = node.nex
        temp_prev = node.prev
        node.nex = None
        node.prev = None
        temp_prev.nex = temp_next
        temp_next.prev = temp_prev
        return node
    
    def insertAtHead(self, node):
        head = self.head
        temp_next = head.nex
        node.prev = head
        head.nex = node
        node.nex = temp_next
        temp_next.prev = node
    
    def removeFromTail(self):
        tail = self.tail 
        end = tail.prev
        new_end = end.prev
        end.nex = None
        end.prev = None
        tail.prev = new_end
        new_end.nex = tail
        return end


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.freq_dll = {}  # map of freq -> Dll()
        self.node_map = {}  # key -> DllNode
        self.min_freq = 0   # Track minimum frequency for O(1) eviction
        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1 
        
        node = self.node_map[key]
        self.updateNodeDll(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.updateNodeDll(node)
        else:
            # Evict BEFORE inserting if we are at capacity
            if len(self.node_map) == self.cap:
                self.evictNode()

            node = DllNode(key, value)
            self.node_map[key] = node
            self.updateNodeDll(node)

    def updateNodeDll(self, node):
        prev_freq = node.freq
        
        if prev_freq != 0:
            prev_dll = self.freq_dll[prev_freq]
            prev_dll.remove(node)
            prev_dll.length -= 1  # Fixed typo (= -1 to -= 1)
            
            # If the min_freq list becomes empty, increment min_freq
            if prev_freq == self.min_freq and prev_dll.length == 0:
                self.min_freq += 1

        # Update frequency
        new_freq = prev_freq + 1
        node.freq = new_freq
        
        if new_freq not in self.freq_dll:
            self.freq_dll[new_freq] = Dll()

        new_dll = self.freq_dll[new_freq]
        new_dll.insertAtHead(node)
        new_dll.length += 1
        
        # If it's a brand new node, its freq is 1, so min_freq must become 1
        if prev_freq == 0:
            self.min_freq = 1

    def evictNode(self):
        # Directly target the min_freq list in O(1) time
        freq_dll = self.freq_dll[self.min_freq]
        removed_node = freq_dll.removeFromTail()
        freq_dll.length -= 1  # Fixed missing decrement
        
        del self.node_map[removed_node.key]