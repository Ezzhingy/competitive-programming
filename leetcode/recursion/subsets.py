class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, temp):
            sorted_temp = temp.copy()
            sorted_temp.sort()
            
            if sorted_temp not in res: # checks if this current combo exists
                res.append(sorted_temp) # appends sorted version to keep checking against
            if len(temp) == len(nums):
                return
    
            for i in range(start, len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                
                    backtrack(start + 1, temp)
                    temp.pop()
        
        backtrack(0, [])
        return res
    
    # a better solution that takes less space would be to have an outside for loop
    # dictating the len(temp), instead of going all the way through the
    # inner for loop
        