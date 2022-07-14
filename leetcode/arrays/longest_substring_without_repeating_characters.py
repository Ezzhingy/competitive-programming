class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        # define length of longest substring
        length_longest_substring = 0
        
        # define start and end pointers
        start, end = 0, 0
        
        hash_table = {}
        
        while end < len(s):
            if s[end] not in hash_table:
                hash_table[s[end]] = 1
            
            else:
                # end increases at the end anyway, decrease it here to reset
                end -= 1
                
                if (end - start + 1) > length_longest_substring:
                    length_longest_substring = end - start + 1
                
                hash_table.pop(s[start])
                start += 1
                            
            end += 1
            
        if len(s) == 1:
            length_longest_substring = 1
        
        # go back to previous end
        end -= 1
        if (end - start + 1) > length_longest_substring and hash_table[s[end]] == 1:
            length_longest_substring = end - start + 1
            
        return length_longest_substring
        