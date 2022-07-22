class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n)
        
        s = s.lower()
        s = s.strip()
        new_string = ""
        
        for c in s:
            if c in string.ascii_lowercase or c in "1234567890":
                new_string += c
        
        return new_string == new_string[::-1]
        
        