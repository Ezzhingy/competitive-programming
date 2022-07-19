class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # o(n^2)
#         total = -math.inf
        
#         if len(nums) == 1:
#             return nums[0]
        
#         for i in range(len(nums)):
#             current_sum = nums[i]
#             if current_sum > total:
#                 total = current_sum            
                
#             for j in range(i + 1, len(nums)):
#                 current_sum += nums[j]
                
#                 if current_sum > total:
#                     total = current_sum
        
#         return total

        # if prefix < index, get rid of prefix
        # similar to a sliding window problem
        # o(n)
        total = -math.inf
        current_sum = 0

        for i in range(len(nums)):
            if i == 0:
                current_sum += nums[i]
            else:   
                if current_sum < nums[i] and current_sum < 0:
                    current_sum = nums[i]
                else:
                    current_sum += nums[i]
            
            total = max(total, current_sum)
        
        return total
                
                
        
        
        