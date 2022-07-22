class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sort() function O(mnlogn)
        
#         hash_map = defaultdict(list) # used to escape index errors
        
#         for s in strs:
#             temp = list(s)
#             temp.sort()
#             anagram = "".join(temp)
#             hash_map[anagram].append(s)
            
#         return hash_map.values()
    
        # O(mn) approach 
        hash_map = defaultdict(list) # used to escape index errors
        
        for s in strs:
            count = [0] * 26
            for c in s:
                char_num = ord(c) - ord('a')
                count[char_num] += 1
            # should now have a list 'count' with indexes += 1 at letter indices
            hash_map[tuple(count)].append(s) # if words have same count configuration
        
        return hash_map.values()
                                        
            
        