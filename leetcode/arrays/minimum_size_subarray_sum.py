class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if this length doesn't change, means there is no answer, return 0
        length_of_minimal_subarray = len(nums) + 1
        
        start, end = 0, 0
        
        total = 0
        
        while end < len(nums):
            if total + nums[end] < target:
                total += nums[end]
            
            else:
                # this total is now > target
                total += nums[end]
                
                while total >= target:
                    if (end - start + 1) < length_of_minimal_subarray:
                        length_of_minimal_subarray = end - start + 1
                    total -= nums[start]
                    start += 1
            
            end += 1
        
        if length_of_minimal_subarray == len(nums) + 1:
            length_of_minimal_subarray = 0
        return length_of_minimal_subarray
            