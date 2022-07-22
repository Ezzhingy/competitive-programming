class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # used hash table and compared both strings to see if they had their                 # individual spot in hash table
        # O(n)
#         hash_table = defaultdict(list)
        
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         hash_table[tuple(count)].append(s)
        
#         count = [0] * 26
#         for c in t:
#             count[ord(c) - ord('a')] += 1
#         hash_table[tuple(count)].append(t)
        
#         return True if len(hash_table) == 1 else False
        
        # easier solution: use hash table for first string, subtract
        # for second string, check to see if hash table values all 0
        # O(n)
        hash_table = {}
        
        for c in s:
            if c not in hash_table:
                hash_table[c] = 1
            else:
                hash_table[c] += 1
        
        for c in t:
            if c in hash_table:
                hash_table[c] -= 1
            else:
                return False
        
        for value in hash_table.values():
            if value != 0:
                return False
        return True
            
        