class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using bubble sort --> side by side comparison, swap if larger
        
        # optimization --> sort can end early if swapped stays False
        swapped = True
        
        # optimization --> after each iteration decrease last unsorted num by one
        last_unsorted_num = len(nums) - 1
        
        while swapped:
        
            swapped = False
            
            for i in range(last_unsorted_num):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    
                    swapped = True
            
            last_unsorted_num -= 1
