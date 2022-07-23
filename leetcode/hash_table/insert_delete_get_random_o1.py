class RandomizedSet:
    # remember that list does NOT have to be in order

    def __init__(self):
        self.list = []
        self.hash_table = {}

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            self.hash_table[val] = len(self.list)
            self.list.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.hash_table: # assume [1,2,3,4] and val = 2
            index = self.hash_table[val] # index = 1
            last_value = self.list[-1] # last_value = 4
            self.list[index] = last_value # [1,4,3,4]
            self.list.pop() # [1,4,3]
            self.hash_table[last_value] = index
            del self.hash_table[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()