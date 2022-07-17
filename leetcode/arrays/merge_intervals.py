class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort() # O(nlogn)
        
        merged = [] # [start, end]
        merged.append(intervals[0])
        
        for i in intervals:
            # if the end of back value is >= the start of the front value,
            # take the max of their back values
            if merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1], i[1])
                
            else:   
                merged.append(i)
        
        return merged
        