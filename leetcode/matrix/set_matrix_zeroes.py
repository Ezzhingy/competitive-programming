class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # O(mn) time complexity
        # O(m) space complexity
        zero_lst = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] != 0:
                        matrix[i][j] = 0
                    else:
                        zero_lst.append(j)
        
        for i in range(len(zero_lst)):
            for j in range(len(matrix)):
                matrix[j][zero_lst[i]] = 0
                    
                