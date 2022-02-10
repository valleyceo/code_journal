class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for _ in range(1000)]
        
    def getHash(self, key: int) -> int:
        return key % 997

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hkey = self.getHash(key)
        
        for i in range(len(self.arr[hkey])):
            if self.arr[hkey][i][0] == key:
                self.arr[hkey][i][1] = value
                return
        
        self.arr[hkey].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hkey = self.getHash(key)
        
        for i in range(len(self.arr[hkey])):
            if self.arr[hkey][i][0] == key:
                return self.arr[hkey][i][1]
        
        return -1
    
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hkey = self.getHash(key)
        for i in range(len(self.arr[hkey])):
            if self.arr[hkey][i][0] == key:
                self.arr[hkey][i], self.arr[hkey][-1] = self.arr[hkey][-1], self.arr[hkey][i]
                self.arr[hkey].pop()
                break
                