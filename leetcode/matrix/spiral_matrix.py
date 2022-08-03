class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # O(mn) running time
        # O(1) space complexity
        res = []
        
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        
        while left <= right:
            start = left
            
            # go right
            while start <= right:
                res.append(matrix[top][start])
                start += 1
            
            if len(res) == len(matrix) * len(matrix[0]): break
            
            # go down
            top += 1
            start = top
            while start <= bottom:
                res.append(matrix[start][right])
                start += 1
            
            if len(res) == len(matrix) * len(matrix[0]): break
                
            # go left
            right -= 1
            start = right
            while start >= left:
                res.append(matrix[bottom][start])
                start -= 1
                
            if len(res) == len(matrix) * len(matrix[0]): break
                
            # go up
            bottom -= 1
            start = bottom
            while start >= top:
                res.append(matrix[start][left])
                start -= 1
            
            left += 1
        
        return res
            