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
        return
        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1 
        
        # insert at head 
        node = self.node_map[key]
        self.remove(node)
        self.insertAtHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.node_map:
            node = DllNode(key,value)
            self.node_map[key] = node
        else:
            # remove 
            self.remove(self.node_map[key])

        # already removed.
        node = self.node_map[key]   
        # update node value 
        node.val = value

        self.insertAtHead(node)

        # now check if the capacity is more then flush out not needed ones
        if len(self.node_map) > self.capacity:
            self.removeAtTail()

        # return node.val

    def remove(self,node):
        nex_node = node.nex
        prev_node = node.prev

        # wire up the dll connections
        node.nex = None
        node.prev = None

        prev_node.nex = nex_node
        nex_node.prev = prev_node


    def insertAtHead(self,node):
        head = self.head 
        # insert at head 
        tmp_next= head.nex

        head.nex = node
        node.prev = head

        tmp_next.prev = node
        node.nex = tmp_next

    def removeAtTail(self):
        tail = self.tail
        end = self.tail.prev

        new_end = end.prev

        # wire up
        end.nex = None
        end.prev = None

        # wire remaining 
        tail.prev = new_end
        new_end.nex = tail

        del self.node_map[end.key]



   