class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(10000)]
        
    def getHash(self, key: int) -> int:
        return key % 9973
        
    def add(self, key: int) -> None:
        hkey = self.getHash(key)
        
        if key not in self.arr[hkey]:
            self.arr[hkey].append(key)

    def remove(self, key: int) -> None:
        hkey = self.getHash(key)
        
        if key in self.arr[hkey]:
            self.arr[hkey].remove(key)

    def contains(self, key: int) -> bool:
        hkey = self.getHash(key)
        return key in self.arr[hkey]