class MyHashSet:

    def __init__(self):
        self.map = []

    def add(self, key: int) -> None:
        if key not in self.map:
            self.map.append(key)
        

    def remove(self, key: int) -> None:
        if key not in self.map:
            return
        self.map.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.map
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)