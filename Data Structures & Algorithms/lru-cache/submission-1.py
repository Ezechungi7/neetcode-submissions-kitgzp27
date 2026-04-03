class Node:
    def __init__(self,key, val):
        self.next = self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self,node):
        prv, nxt = self.right.prev,self.right
        prv.next = nxt.prev = node # -> node <-
        node.next, node.prev = nxt, prv # <- node ->

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #could just update pointers, but this approach is simpler to write and read
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            last = self.left.next
            self.remove(last)
            del self.cache[last.key]
 
        


        
