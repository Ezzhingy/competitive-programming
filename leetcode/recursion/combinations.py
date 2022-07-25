class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        # backtracking solution
        
        res = []
        
        def recursive(start, nums):
            if len(nums) == k:
                res.append(nums.copy())
                return # since this stops run, no unnecessary loop is made
            
            for i in range(start, n + 1): 
                # loops through each number, each recursion adds a smaller loop
                nums.append(i)
                recursive(i+1, nums)
                nums.pop() # once recursion is done (return), next loop is undergone
                           # [1,2], 2 is popped, small loop on 3, big loop on 1
        recursive(1, [])
        return res
            