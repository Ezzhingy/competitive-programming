class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use result list to store all prefix products, then multiply that 
        # by all postfix products
        
        result = len(nums) * [1]
        prefix, postfix = 1, 1
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result