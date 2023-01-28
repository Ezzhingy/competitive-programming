class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # need to recurse somehow, given new image, new sr, sc, same color
        if image[sr][sc] == color:
            return image
            
        find_color = image[sr][sc] 
        self.newFill(image, sr, sc, find_color, color) 
        return image

    def newFill(self, image, sr, sc, need_color, new_color):
        if sr >= len(image) or sc >= len(image[0]) or sr < 0 or sc < 0 or image[sr][sc] != need_color:
            return None

        image[sr][sc] = new_color
        self.newFill(image, sr, sc - 1, need_color, new_color)
        self.newFill(image, sr, sc + 1, need_color, new_color)
        self.newFill(image, sr - 1, sc, need_color, new_color)
        self.newFill(image, sr + 1, sc, need_color, new_color)        
        

        # [[1,1,1],
        #  [1,1,0],
        #  [1,0,1]]
        # ORIGINAL: sr = 1, sc = 1
        # sr = 1, sc = 0
        # sr = 1, sc = 2
        # sr = 0, sc = 1
        # sr = 2, sc = 1

        # color = 2
        # [[2,2,2],
        #  [2,2,0],
        #  [2,0,1]]
