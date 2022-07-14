class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # two pointers approach, using start and end to define regions
        
        count = 0
        
        for start in range(0, len(s)):
            for end in range(start + 1, len(s) + 1):
                substring_of_s = s[start : end]
                reverse_string = substring_of_s[::-1]
                
                if substring_of_s == reverse_string:
                    count += 1
                
        return count