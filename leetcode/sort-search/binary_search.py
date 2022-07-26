class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # both solutions work
        
        p1, p2 = 0, len(nums) - 1
#         mid = (p1 + p2) // 2

#         while nums[mid] != target:
#             mid = math.floor((p1 + p2) / 2)
            
#             if p1 > p2:
#                 return -1
            
#             elif nums[mid] < target:
#                 p1 = mid + 1
            
#             elif nums[mid] > target:
#                 p2 = mid - 1
                    
#         return mid

        while p1 <= p2:
            mid = (p1 + p2) // 2
            
            if nums[mid] > target:
                p2 = mid - 1
            
            elif nums[mid] < target:
                p1 = mid + 1
            
            elif nums[mid] == target:
                return mid
        
        return -1

            
            