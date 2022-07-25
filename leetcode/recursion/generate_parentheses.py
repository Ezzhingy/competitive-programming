class Solution:        
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Code credit to NeetCode
        
        def recursive(open_count, closed_count):
            if open_count == n and closed_count == n:
                res.append("".join(temp))
                return

            if open_count < n:
                temp.append("(")
                recursive(open_count + 1, closed_count) # looks at all open parentheses possibilities first
                temp.pop() # after they are all considered, removes one and looks at next conditional

            if open_count > closed_count:
                temp.append(")")
                recursive(open_count, closed_count + 1)
                temp.pop()
                
        res = []
        temp = []
        
        recursive(0, 0)
        
        return res