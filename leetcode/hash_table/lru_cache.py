# Code inspired by NeetCode
# His idea: Double linked list + hash table
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.least_recent, self.most_recent = Node(0, 0), Node(0, 0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent
        
        self.hash_table = {}
        
    def remove(self, node): # moves prev and next pointers around to 'remove' node
                            # from linked list
        current_prev, current_next = node.prev, node.next
        current_prev.next = current_next
        current_next.prev = current_prev 
    
    def insert(self, node): # same concept as remove
        current_prev, current_next = self.most_recent.prev, self.most_recent
        node.prev, current_prev.next = current_prev, node
        node.next, self.most_recent.prev = self.most_recent, node
            
    def get(self, key: int) -> int:
        if key in self.hash_table: # make sure to re-insert node since it was 'used'
            self.remove(self.hash_table[key])
            self.insert(self.hash_table[key])
            return self.hash_table[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.remove(self.hash_table[key]) # removes the node to be added later
                                              # since the hash table's values are
                                              # pointers, no need to change table
        
        self.hash_table[key] = Node(key,value)
        self.insert(self.hash_table[key])
        
        if len(self.hash_table) > self.capacity:
            del self.hash_table[self.least_recent.next.key]
            self.remove(self.least_recent.next)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)