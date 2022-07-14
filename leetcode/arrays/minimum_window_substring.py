class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s is main string
        # t us smaller string
        
        #create hash table for t string
        hash_table = {}
        for t_char in t:
            if t_char not in hash_table:
                hash_table[t_char] = 1
            else:
                hash_table[t_char] += 1
        
        # if this value does not change, return ""
        minimum_length_substring = len(s) + 1
        
        # required number of chars needed in t
        required_chars_t = len(t)
        
        start, end = 0, 0
        smallest_start, smallest_end = 0, 0
        
        while end < len(s):
            # look at end value
            if s[end] in hash_table:
                
                # check to see if char is needed
                if hash_table[s[end]] > 0:
                    required_chars_t -= 1
                
                # even if char is not needed, subtract anyway, 
                # can use < 0 info later
                hash_table[s[end]] -= 1
            
            # once window is fulfilled
            while required_chars_t == 0:
                # check to see if length of this window is less than before
                if (end - start + 1) < minimum_length_substring:
                    minimum_length_substring = end - start + 1
                    
                    smallest_start = start
                    smallest_end = end
                
                # before incrementing start, check to see if start was important
                if s[start] in hash_table:
                    
                    # only relevant value if this character is 0 in hash table
                    if hash_table[s[start]] == 0:
                        # give that char back
                        hash_table[s[start]] += 1
                        required_chars_t += 1
                    
                    # if important char is already in substring
                    elif hash_table[s[start]] < 0:
                        hash_table[s[start]] += 1
                               
                # increment start up one
                start += 1
                
            # otherwise increase end
            end += 1
        
        # if minimum_length_substring did not change
        if minimum_length_substring == len(s) + 1:
            return ""
        return s[smallest_start : smallest_end + 1]
                    
        