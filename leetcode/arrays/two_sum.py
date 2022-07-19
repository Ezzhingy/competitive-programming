class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map solution
        hash_map = {}
        
        for index, num in enumerate(nums):            
            difference = target - num
            
            if difference in hash_map.keys():
                return [index, hash_map[difference]]
            
            hash_map[num] = index
