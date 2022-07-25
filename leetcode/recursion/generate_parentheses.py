class Solution:        
    def generateParenthesis(n):
        
        # Code credit to NeetCode
        
        def recursive(open_count, closed_count):
            if open_count == n and closed_count == n:
                res.append("".join(temp))
                return

            if open_count < n:
                temp.append("(")
                recursive(open_count + 1, closed_count) # looks at all open parentheses possibilities first
                temp.pop() # after they are all considered, removes one and looks at next conditional
                           # will add any possible ')' next, looking at all possibilities

            if open_count > closed_count:
                temp.append(")")
                recursive(open_count, closed_count + 1) # will always be the last recursion
                temp.pop() # removes all rightmost ')'
                
        res = []
        temp = []
        
        recursive(0, 0)
        
        return res