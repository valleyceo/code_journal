"""
LC 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
"""
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class DoublyLinkedList():
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
class LRUCache:

    def __init__(self, capacity: int):
        self.kmap = {}
        self.dll = DoublyLinkedList()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.kmap:
            node = self.kmap[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kmap:
            node = self.kmap[key]
            
            self.removeNode(node)
            node.val = value
            self.addNode(node)
        else:
            if self.capacity == len(self.kmap):
                last_node = self.dll.tail.prev
                self.removeNode(last_node)
                del self.kmap[last_node.key]
                
            node = Node(key, value)
            self.addNode(node)
            self.kmap[key] = node
            
    def addNode(self, node: Node):
        next_node = self.dll.head.next
        self.dll.head.next = node
        node.prev = self.dll.head
        
        node.next = next_node
        next_node.prev = node
    
    def removeNode(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)