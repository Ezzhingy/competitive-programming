class Solution:
    def longestPalindrome(self, s: str) -> str:
        # code credit goes to NeetCode, inspired by his own algorithm + code


        longest_sub = ""
        length = 0
                
        for i in range(len(s)):
            # odd
            p1, p2 = i, i
            
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > length:
                    length = p2 - p1 + 1
                    longest_sub = s[p1:p2 + 1]
                p1 -= 1
                p2 += 1
            
            # even
            p1, p2 = i, i + 1
            
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > length:
                    length = p2 - p1 + 1
                    longest_sub = s[p1:p2 + 1]
                p1 -= 1
                p2 += 1
        
        return longest_sub
                    
                    