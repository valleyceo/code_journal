# LC 460. LFU Cache

'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''

class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.max_cap = capacity
        self.min_freq = 0
        self.key_map = {}
        self.freq_list = defaultdict(DLL)

    def update(self, node):
        freq = node.freq
        self.freq_list[freq].pop(node)

        if self.min_freq == freq and not self.freq_list[freq]:
            self.min_freq += 1 # if freq == min_freq, the next upper min_freq is always freq+1 (which is itself)

        node.freq += 1
        freq = node.freq
        self.freq_list[freq].append(node)

    def get(self, key: int) -> int:

        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if self.max_cap == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.max_cap:
                node = self.freq_list[self.min_freq].pop()
                del self.key_map[node.key]
                self.size -= 1

            node = Node(key, value)
            self.key_map[key] = node
            self.freq_list[1].append(node)
            self.min_freq = 1
            self.size += 1

class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.root.next
        node.prev = self.root
        node.next.prev = node
        self.root.next = node
        self.size += 1

    def pop(self, node = None):
        if self.size == 0:
            return

        if not node:
            node = self.root.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Key Insights:
- You need 2 data structures for LRU/LFU:
    - Key/Value dictionary
    - Most recent list (freq/DLL dictionary)
- Frequency List (with least recent if even)
    - Key is the frequency, value is DLL of nodes (which stores key, value, frequency)
- Update method:
    - Increments the node freq in list
        - Remove and add into the freq/DLL map
"""
