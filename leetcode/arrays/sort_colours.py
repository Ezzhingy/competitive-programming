class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # using two pointers approach
        
        # start pointer and end pointer
        start = 0
        end = len(nums) - 1
        
        increment = 0
        
        while increment <= end:
            if nums[increment] == 0:
                nums[increment], nums[start] = nums[start], nums[increment]
                
                start += 1
                
            if nums[increment] == 2:
                nums[increment], nums[end] = nums[end], nums[increment]

                end -= 1
                
                # instead of incrementing here, go again
                continue
                
            increment += 1
