class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hash table
        hash_table = {}
        for c in ransomNote:
            if c not in hash_table:
                hash_table[c] = 1
            else:
                hash_table[c] += 1
        
        for c in magazine:
            if c in hash_table:
                hash_table[c] -= 1
            
        for value in hash_table.values():
            if value > 0: return False
            
        return True 